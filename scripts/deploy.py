"""Publish a complete static snapshot and atomically select it for Nginx."""

import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path


root = Path('/var/www/sindri-observatory')
commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
release = Path(tempfile.mkdtemp(prefix=f'{commit[:12]}-', dir=root / 'releases'))
release.chmod(0o755)
next_link = root / f'next-{release.name}'

try:
    for name in ('index.html', 'runner-status.css', 'runner-status.js'):
        shutil.copy2(name, release / name)
    shutil.copytree('data', release / 'data')
    record = {
        'commit': commit,
        'deployed_at': datetime.now(timezone.utc).isoformat(),
        'run_id': os.environ['GITHUB_RUN_ID'],
        'run_attempt': os.environ['GITHUB_RUN_ATTEMPT'],
    }
    (release / 'deployment.json').write_text(json.dumps(record, indent=2) + '\n')
    next_link.symlink_to(release.relative_to(root), target_is_directory=True)
    os.replace(next_link, root / 'current')
except BaseException:
    next_link.unlink(missing_ok=True)
    shutil.rmtree(release)
    raise

print(json.dumps(record, indent=2))
