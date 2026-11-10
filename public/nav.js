(() => {
  "use strict";
  // Mobile menu
  const btn = document.querySelector(".menu-btn"), menu = document.getElementById("mnav");
  if (btn && menu) {
    const set = (open) => { menu.hidden = !open; btn.setAttribute("aria-expanded", open); btn.setAttribute("aria-label", open ? "Close menu" : "Open menu"); };
    btn.addEventListener("click", (e) => { e.stopPropagation(); set(menu.hidden); });
    document.addEventListener("click", (e) => { if (!menu.hidden && !menu.contains(e.target)) set(false); });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !menu.hidden) { set(false); btn.focus(); } });
    menu.addEventListener("click", (e) => { if (e.target.closest("a")) set(false); });
  }
  // Header dropdowns (Product, Solutions)
  const hover = matchMedia("(hover: hover) and (pointer: fine)");
  const all = [...document.querySelectorAll(".dd")];
  all.forEach((dd) => {
    const b = dd.querySelector(".dd-btn"), panel = dd.querySelector(".dd-panel");
    if (!b || !panel) return;
    let t = 0, hoverAt = 0;
    const set = (open) => {
      clearTimeout(t);
      if (open) all.forEach((o) => { if (o !== dd && o.classList.contains("open")) { o.classList.remove("open"); o.querySelector(".dd-btn").setAttribute("aria-expanded", false); } });
      dd.classList.toggle("open", open); b.setAttribute("aria-expanded", open);
    };
    b.addEventListener("click", () => set(Date.now() - hoverAt < 400 ? true : !dd.classList.contains("open")));
    dd.addEventListener("mouseenter", () => { if (hover.matches) { if (!dd.classList.contains("open")) hoverAt = Date.now(); set(true); } });
    dd.addEventListener("mouseleave", () => { if (hover.matches) t = setTimeout(() => set(false), 160); });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && dd.classList.contains("open")) { set(false); b.focus(); } });
    document.addEventListener("click", (e) => { if (!dd.contains(e.target)) set(false); });
    dd.addEventListener("focusout", (e) => { if (!dd.contains(e.relatedTarget)) set(false); });
    panel.addEventListener("click", (e) => { if (e.target.closest("a")) set(false); });
  });
})();
