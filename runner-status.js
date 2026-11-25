const message = document.getElementById('runner-message');
const runLink = document.getElementById('runner-run');
const updatedAt = document.getElementById('runner-time');
const dateFormat = new Intl.DateTimeFormat('en-GB', {
  dateStyle: 'medium',
  timeStyle: 'medium',
  timeZone: 'UTC',
});

async function refreshRunnerStatus() {
  try {
    const response = await fetch('data/runner-demo.json', {
      cache: 'no-store',
      signal: AbortSignal.timeout(10000),
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const record = await response.json();
    if (record.schema_version !== 1 || typeof record.message !== 'string') {
      throw new Error('Invalid runner status');
    }

    if (message.textContent !== record.message) message.textContent = record.message;
    runLink.hidden = !record.run_id;
    if (record.run_id) {
      runLink.href = `https://github.com/lvjx04/sindri-observatory/actions/runs/${encodeURIComponent(record.run_id)}`;
      runLink.textContent = `Run ${record.run_id} · attempt ${record.run_attempt}`;
    }
    updatedAt.textContent = record.created_at
      ? `${dateFormat.format(new Date(record.created_at))} UTC`
      : '';
  } catch {
    message.textContent = 'Runner status unavailable';
    runLink.hidden = true;
    updatedAt.textContent = '';
  }
}

refreshRunnerStatus();
setInterval(refreshRunnerStatus, 15000);
