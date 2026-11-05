// "Try a call": the endpoint buttons swap the sample request and response. All data is illustrative.
(() => {
  const btns = document.querySelectorAll('#playground .seg button');
  const req = document.getElementById('pl-req');
  const res = document.getElementById('pl-res');
  if (!btns.length || !req || !res) return;
  const cost = document.getElementById('pl-cost');
  const note = document.getElementById('pl-note');
  const status = document.getElementById('pl-status');
  const ask = document.getElementById('pl-ask');

  const EP = {
    search: {
      ask: '“Find independent orthopedic surgeons in Arizona.”',
      cost: '0.05 credits per result',
      note: 'The agent searches wide, then calls enrich_provider only on the matches it keeps.',
      status: 'ok',
      req: `{
  "method": "tools/call",
  "params": {
    "name": "search_providers",
    "arguments": {
      "specialty": "orthopedic surgery",
      "state": "AZ",
      "affiliation_type": "independent_group",
      "limit": 3
    }
  }
}`,
      res: {
        total: 412, credits_used: 0.15,
        results: [
          { npi: '1234567890', name: 'Dr. Jane Example, MD', city: 'Phoenix', group: 'Example Ortho Partners' },
          { npi: '1234567891', name: 'Dr. Sam Sample, DO', city: 'Tucson', group: 'Desert Spine Group' },
          { npi: '1234567892', name: 'Dr. Lee Placeholder, MD', city: 'Mesa', group: 'Valley Joint Clinic' }
        ]
      }
    },
    enrich: {
      ask: '“What licenses and affiliations does Dr. Jane Example have?”',
      cost: '1 credit + optional fields',
      note: 'Ask for contact or network fields only when you need them. Each one adds a credit.',
      status: 'ok',
      req: `{
  "method": "tools/call",
  "params": {
    "name": "enrich_provider",
    "arguments": {
      "npi": "1234567890",
      "fields": ["licenses", "affiliations", "practice_contact"]
    }
  }
}`,
      res: {
        npi: '1234567890', name: 'Dr. Jane Example, MD', specialty: 'Orthopedic Surgery',
        licenses: [
          { state: 'AZ', status: 'active', source: 'state_board', verified: '2026-11-02' },
          { state: 'NV', status: 'active', source: 'state_board', verified: '2026-11-02' }
        ],
        affiliations: [
          { org: 'Example Ortho Partners', since: '2024-03', source: 'practice_website' },
          { org: 'Sample Regional Medical Center', source: 'cms_provider_data' }
        ],
        practice_contact: { phone: '(555) 010-0199', source: 'practice_website', verified: '2026-11-05' },
        credits_used: 2
      }
    },
    org: {
      ask: '“Who leads Example Health System, and are they hiring?”',
      cost: '2 credits',
      note: 'Organizations come with locations, rostered clinicians, leadership and open roles.',
      status: 'ok',
      req: `{
  "method": "tools/call",
  "params": {
    "name": "enrich_org",
    "arguments": { "name": "Example Health System", "state": "AZ" }
  }
}`,
      res: {
        org_id: 'org_7f3a', name: 'Example Health System', type: 'health_system',
        locations: 14, rostered_clinicians: 1180,
        children: ['Sample Regional Medical Center', 'Example Heart Group', '+12 more'],
        leadership: [{ role: 'Chief Medical Officer', name: 'Dr. Alex Sample', since: '2026-10' }],
        open_clinical_roles: 63,
        signals: [{ type: 'org.hiring_spike', detected: '2026-11-03' }],
        credits_used: 2
      }
    },
    watch: {
      ask: '“Tell me if any of these surgeons change groups.”',
      cost: '0.5 credits per event delivered',
      note: 'Your agent creates the watch once. Changes arrive as notifications, or by webhook to your backend.',
      status: 'ok',
      req: `{
  "method": "tools/call",
  "params": {
    "name": "watch_providers",
    "arguments": {
      "npis": ["1234567890", "1234567891"],
      "events": ["affiliation.changed", "license.issued"]
    }
  }
}`,
      res: {
        watcher_id: 'wch_21b9', status: 'active', watching: 2,
        sample_event: {
          type: 'affiliation.changed', npi: '1234567890',
          from: 'Example Ortho Partners', to: 'Northfield Spine Partners',
          source: 'practice_website', detected: '2026-11-05T07:26:00Z'
        }
      }
    }
  };

  const esc = s => s.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const paint = obj => esc(JSON.stringify(obj, null, 2))
    .replace(/(&quot;|")([^"]+)"(?=:)/g, '<span class="k">"$2"</span>')
    .replace(/: "([^"]*)"/g, ': <span class="s">"$1"</span>')
    .replace(/: (-?\d+(?:\.\d+)?)/g, ': <span class="n">$1</span>');

  const set = key => {
    const e = EP[key];
    btns.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.ep === key)));
    req.textContent = e.req;
    res.innerHTML = paint(e.res);
    cost.textContent = e.cost;
    note.textContent = e.note;
    status.textContent = e.status;
    if (ask) ask.textContent = e.ask;
  };
  btns.forEach(b => b.addEventListener('click', () => set(b.dataset.ep)));
  set('search');
})();
