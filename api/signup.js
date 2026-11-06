// POST /api/signup: store a trial signup as a private JSON blob.
import { put } from "@vercel/blob";

const USE_CASES = ["medtech-pharma", "provider-directory", "staffing", "investing", "digital-health", "other"];
const CLIENTS = ["claude", "cursor", "chatgpt", "other-mcp", "rest-api"];
const FREE_MAIL = /@(gmail|yahoo|hotmail|outlook|icloud|aol|proton(mail)?|live|me)\./i;

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json", "cache-control": "no-store" } });

const clean = (v, max = 200) => String(v ?? "").replace(/[\u0000-\u001f]/g, " ").trim().slice(0, max);

export async function POST(request) {
  let data;
  try {
    const type = request.headers.get("content-type") || "";
    data = type.includes("application/json") ? await request.json() : Object.fromEntries(await request.formData());
  } catch {
    return json({ ok: false, error: "Could not read the form." }, 400);
  }
  if (clean(data.website)) return json({ ok: true }); // honeypot: bots fill hidden fields

  const email = clean(data.email, 160).toLowerCase();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return json({ ok: false, error: "Please enter a valid work email." }, 422);
  const name = clean(data.name, 120);
  if (!name) return json({ ok: false, error: "Please tell us your name." }, 422);

  const record = {
    ts: new Date().toISOString(),
    name,
    email,
    company: clean(data.company, 160),
    use_case: USE_CASES.includes(data.use_case) ? data.use_case : "other",
    client: CLIENTS.includes(data.client) ? data.client : "other-mcp",
    note: clean(data.note, 1000),
    free_mail: FREE_MAIL.test(email),
    source: clean(data.source, 300),
    referrer: clean(request.headers.get("referer"), 300),
    country: clean(request.headers.get("x-vercel-ip-country"), 8),
  };

  try {
    await put(`signups/${record.ts.slice(0, 10)}/${email.replace(/[^a-z0-9@._-]/g, "_")}.json`, JSON.stringify(record), {
      access: "private",
      contentType: "application/json",
      addRandomSuffix: true,
    });
  } catch (err) {
    console.error("signup store failed", err);
    return json({ ok: false, error: "Something went wrong on our side. Please try again." }, 500);
  }
  return json({ ok: true });
}

export function GET() {
  return json({ ok: false, error: "Use POST." }, 405);
}
