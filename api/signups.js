// GET /api/signups?key=...  (HTML table)   &format=csv  (download)
import { list, get } from "@vercel/blob";

const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const COLS = ["ts", "name", "email", "company", "use_case", "client", "note", "free_mail", "source", "referrer", "country"];

export async function GET(request) {
  const url = new URL(request.url);
  const key = process.env.SIGNUPS_ADMIN_KEY;
  if (!key || url.searchParams.get("key") !== key) return new Response("Not found", { status: 404 });

  const blobs = [];
  let cursor;
  do {
    const page = await list({ prefix: "signups/", cursor, limit: 1000 });
    blobs.push(...page.blobs);
    cursor = page.hasMore ? page.cursor : undefined;
  } while (cursor);

  const rows = (
    await Promise.all(
      blobs.map(async (b) => {
        try {
          const r = await get(b.pathname, { access: "private" });
          return r && r.stream ? JSON.parse(await new Response(r.stream).text()) : null;
        } catch {
          return null;
        }
      })
    )
  ).filter(Boolean).sort((a, b) => (a.ts < b.ts ? 1 : -1));

  const headers = { "cache-control": "no-store", "x-robots-tag": "noindex" };
  if (url.searchParams.get("format") === "csv") {
    const q = (v) => `"${String(v ?? "").replace(/"/g, '""')}"`;
    const csv = [COLS.join(","), ...rows.map((r) => COLS.map((c) => q(r[c])).join(","))].join("\n");
    return new Response(csv, { headers: { ...headers, "content-type": "text/csv", "content-disposition": "attachment; filename=stethos-signups.csv" } });
  }
  const work = rows.filter((r) => !r.free_mail).length;
  const html = `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Stethos signups</title>
<style>body{font:14px/1.45 system-ui,sans-serif;margin:24px;color:#111}h1{font-size:22px}table{border-collapse:collapse;width:100%}th,td{text-align:left;padding:8px 10px;border-bottom:1px solid #e5e5e5;vertical-align:top}th{background:#f6f6f3;position:sticky;top:0}.k{display:flex;gap:16px;margin:8px 0 18px}.k b{font-size:24px;display:block}</style>
<h1>Stethos trial signups</h1><div class="k"><div><b>${rows.length}</b>total</div><div><b>${work}</b>work email</div><div><a href="?key=${encodeURIComponent(key)}&format=csv">Download CSV</a></div></div>
<div style="overflow-x:auto"><table><tr>${COLS.map((c) => `<th>${c}</th>`).join("")}</tr>${rows.map((r) => `<tr>${COLS.map((c) => `<td>${esc(r[c])}</td>`).join("")}</tr>`).join("")}</table></div>`;
  return new Response(html, { headers: { ...headers, "content-type": "text/html; charset=utf-8" } });
}
