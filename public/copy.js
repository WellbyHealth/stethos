// Copy buttons (MCP URL, config). Falls back to selecting the text if the clipboard is unavailable.
(() => {
  document.querySelectorAll('.copy-mcp').forEach(b => {
    const label = b.innerHTML;
    b.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(b.dataset.copy); b.textContent = 'Copied ✓'; }
      catch (e) { b.textContent = 'Press ⌘C'; const r = document.createRange(); const c = b.parentElement.querySelector('code,pre'); if (c) { r.selectNodeContents(c); const s = getSelection(); s.removeAllRanges(); s.addRange(r); } }
      setTimeout(() => { b.innerHTML = label; }, 1800);
    });
  });
})();
