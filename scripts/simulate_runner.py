"""Create a visible record for the runner-to-website update demonstration."""

import json
import os
from datetime import datetime, timezone
from pathlib import Path


record = {
    'schema_version': 1,
    'run_id': os.environ['GITHUB_RUN_ID'],
    'run_attempt': os.environ['GITHUB_RUN_ATTEMPT'],
    'created_at': datetime.now(timezone.utc).isoformat(),
    'message': 'Runner demo update received',
}
Path('data/runner-demo.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
