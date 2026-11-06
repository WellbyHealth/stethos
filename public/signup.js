(function () {
  var f = document.getElementById("su-form");
  if (!f) return;
  var done = document.querySelector(".su-done"), err = f.querySelector(".su-err"), btn = f.querySelector(".su-btn");
  var q = new URLSearchParams(location.search);
  var src = [];
  ["plan", "utm_source", "utm_medium", "utm_campaign", "ref"].forEach(function (k) { if (q.get(k)) src.push(k + "=" + q.get(k)); });
  try { if (document.referrer && document.referrer.indexOf(location.host) < 0) src.push("from=" + document.referrer); } catch (e) {}
  f.source.value = src.join("&").slice(0, 300);
  var label = btn.innerHTML;
  function fail(m) { err.textContent = m; err.hidden = false; btn.disabled = false; btn.innerHTML = label; }
  f.addEventListener("submit", function (e) {
    e.preventDefault();
    err.hidden = true;
    if (!f.name.value.trim()) return fail("Please tell us your name."), f.name.focus();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.email.value.trim())) return fail("Please enter a valid work email."), f.email.focus();
    btn.disabled = true; btn.textContent = "Signing you up…";
    var data = {}; new FormData(f).forEach(function (v, k) { data[k] = v; });
    fetch("/api/signup", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return { ok: false }; }); })
      .then(function (j) {
        if (!j.ok) return fail(j.error || "Something went wrong. Please try again.");
        done.querySelector(".su-mail").textContent = data.email;
        f.hidden = true; done.hidden = false; done.focus();
        if (window.va) window.va("event", { name: "signup" });
      })
      .catch(function () { fail("We couldn't reach the server. Check your connection and try again."); });
  });
})();
