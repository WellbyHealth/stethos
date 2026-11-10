(() => {
  "use strict";
  // Use-case library: filter workflows by job (chips) and by team (select).
  const chips = [...document.querySelectorAll(".lib-chip")], sel = document.getElementById("lib-team");
  const groups = [...document.querySelectorAll(".lib-group")], empty = document.querySelector(".lib-empty");
  if (!chips.length || !sel) return;
  let job = "all";
  const apply = () => {
    const team = sel.value; let shown = 0;
    groups.forEach((g) => {
      let n = 0;
      g.querySelectorAll(".lib-card").forEach((c) => { const ok = team === "all" || c.dataset.team === team; c.hidden = !ok; if (ok) n++; });
      const on = (job === "all" || g.dataset.job === job) && n > 0;
      g.hidden = !on; if (on) shown += n;
    });
    if (empty) empty.hidden = shown > 0;
  };
  chips.forEach((b) => b.addEventListener("click", () => {
    job = b.dataset.job; chips.forEach((c) => c.setAttribute("aria-pressed", c === b)); apply();
  }));
  sel.addEventListener("change", apply);
  // Open a linked workflow (e.g. /use-cases#referral-map)
  const open = () => { const el = location.hash && document.getElementById(location.hash.slice(1)); if (el && el.classList.contains("lib-card")) { const d = el.querySelector("details"); if (d) d.open = true; } };
  window.addEventListener("hashchange", open); open();
})();
