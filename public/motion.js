/* Stethos homepage motion: rotating headline word, count-up stats, live sample
   change feed, with/without comparison tabs, and scroll reveals.
   Everything degrades to static content without JS or with reduced motion. */
(function () {
  var still = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var io = "IntersectionObserver" in window;
  document.documentElement.classList.add("mo-js");
  if (still) document.documentElement.classList.add("mo-still");

  function onView(el, fn, threshold) {
    if (!el) return;
    if (!io || still) return fn();
    var o = new IntersectionObserver(function (es) {
      if (es[0].isIntersecting) { o.disconnect(); fn(); }
    }, { threshold: threshold || 0.3 });
    o.observe(el);
  }

  /* 1. Rotating role in the hero headline */
  var rot = document.querySelector("[data-rot]");
  if (rot) {
    var words = rot.querySelectorAll(".rot-w"), k = 0;
    var fit = function () { var on = rot.querySelector(".rot-w.on"); if (on) rot.style.width = on.offsetWidth + "px"; };
    fit(); window.addEventListener("resize", fit);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
  }
  if (rot && !still) {
    setInterval(function () {
      if (document.hidden) return;
      var cur = words[k]; k = (k + 1) % words.length; var nxt = words[k];
      cur.classList.remove("on"); cur.classList.add("off"); cur.setAttribute("aria-hidden", "true");
      nxt.classList.remove("off"); nxt.classList.add("on"); nxt.removeAttribute("aria-hidden");
      rot.style.width = nxt.offsetWidth + "px";
      setTimeout(function () { cur.classList.remove("off"); }, 600);
    }, 2400);
  }

  /* 2. Count-up stats */
  document.querySelectorAll(".cnt").forEach(function (el) {
    var to = +el.dataset.to;
    if (still || !io) { el.textContent = to; return; }
    el.textContent = "0";
    onView(el, function () {
      var t0 = performance.now(), dur = 1200;
      (function tick(t) {
        var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(to * e);
        if (p < 1) requestAnimationFrame(tick);
      })(t0);
    }, 0.6);
  });

  /* 3. Live sample change feed */
  var feed = document.getElementById("feed-list");
  if (feed) {
    var EV = [
      ["affiliation.changed", "Dr. Maya Example joined Northfield Spine Partners", "Phoenix, AZ"],
      ["license.issued", "Jordan Example, NP, licensed in Utah", "Denver, CO"],
      ["network.joined", "Desert Valley Ortho added to a major commercial plan", "Tucson, AZ"],
      ["location.opened", "Example Primary Care opened a Lakewood clinic", "Lakewood, CO"],
      ["org.exec_hire", "Example Health named a new Chief Medical Officer", "Austin, TX"],
      ["org.hiring_spike", "Northfield Spine Partners posted 8 clinical roles", "Phoenix, AZ"],
      ["license.lapsed", "A Nevada license for Dr. Sam Example expired", "Las Vegas, NV"],
      ["network.left", "Lakeside Cardiology dropped out of a Medicaid plan", "Columbus, OH"],
      ["affiliation.changed", "Dr. Priya Example moved to Example Children's", "Seattle, WA"],
      ["location.opened", "Example Imaging opened a site in Mesa", "Mesa, AZ"]
    ];
    var SHOW = 5, n = 0, ages = [];
    function li(ev, age) {
      var el = document.createElement("li");
      el.innerHTML = '<span class="fe-t">' + ev[0] + '</span><b>' + ev[1] + '</b><span class="fe-m">' + ev[2] + ' · <time>' + age + '</time></span>';
      return el;
    }
    function label(m) { return m < 1 ? "just now" : m + " min ago"; }
    for (var i = 0; i < SHOW; i++) { ages.push(3 + i * 4); feed.appendChild(li(EV[i], label(3 + i * 4))); n++; }
    if (!still) {
      onView(feed, function () {
        setInterval(function () {
          if (document.hidden) return;
          ages = ages.map(function (a) { return a + 2; });
          var el = li(EV[n % EV.length], "just now"); n++;
          el.classList.add("in");
          feed.insertBefore(el, feed.firstChild);
          ages.unshift(0);
          while (feed.children.length > SHOW) { feed.removeChild(feed.lastChild); ages.pop(); }
          feed.querySelectorAll("time").forEach(function (t, j) { t.textContent = label(ages[j]); });
        }, 2800);
      }, 0.4);
    }
  }

  /* 4. With / without comparison tabs */
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".df-tabs [role=tab]"));
  function pick(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab, p = document.getElementById(t.getAttribute("aria-controls"));
      t.setAttribute("aria-selected", on); t.tabIndex = on ? 0 : -1;
      if (p) { p.hidden = !on; if (on) { p.classList.remove("play"); void p.offsetWidth; p.classList.add("play"); } }
    });
    if (focus) tab.focus();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener("click", function () { pick(t); stopAuto(); });
    t.addEventListener("keydown", function (e) {
      var d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
      if (d) { e.preventDefault(); pick(tabs[(i + d + tabs.length) % tabs.length], true); stopAuto(); }
    });
  });
  var auto = null;
  function stopAuto() { if (auto) { clearInterval(auto); auto = null; } }
  var df = document.getElementById("difference");
  if (df && tabs.length) {
    onView(df, function () {
      pick(tabs[0]);
      if (still) return;
      var j = 0;
      auto = setInterval(function () { if (document.hidden) return; j = (j + 1) % tabs.length; pick(tabs[j]); }, 7000);
      df.addEventListener("mouseenter", stopAuto, { once: true });
      df.addEventListener("touchstart", stopAuto, { once: true, passive: true });
    }, 0.35);
  }

  /* 5. Scroll reveals */
  if (io && !still) {
    var targets = document.querySelectorAll("main .head, .stats li, .stk-row > li, .pillars li, .roles li, .kpis li, .split-card, .feed, .connect-grid > *, .play-grid, .compare .col");
    var ro = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("rv-in"); ro.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    targets.forEach(function (el, i) {
      var sib = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      el.classList.add("rv"); el.style.setProperty("--rv", Math.min(sib, 5) * 70 + "ms");
      ro.observe(el);
    });
  }
})();
