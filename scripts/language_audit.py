"""Refresh a public-safe language snapshot from authenticated authored commits.

Run after scripts/discovery.py. This local audit reads private metadata and writes
only aggregate source-file touch counts; it never writes repository names or code.
"""
from __future__ import annotations

import collections
import json
from pathlib import Path
from typing import Any
from urllib.parse import quote

from discovery import ACCOUNT, ROOT, gh_list

EXTENSIONS = {'.rs':'Rust','.lua':'Lua','.ts':'TypeScript','.tsx':'TypeScript','.js':'JavaScript','.jsx':'JavaScript','.py':'Python','.swift':'Swift','.vue':'Vue','.sql':'SQL','.css':'CSS','.html':'HTML','.php':'PHP','.sh':'Shell'}
EXCLUDED = ('node_modules/', 'vendor/', 'dist/', 'build/', '.min.', 'lock.')


def language_for_path(filename: str) -> str | None:
    if any(part in filename.lower() for part in EXCLUDED):
        return None
    return EXTENSIONS.get(Path(filename).suffix.lower())


def aggregate_file_touches(commits: list[dict[str, Any]]) -> dict[str, int]:
    counts: collections.Counter[str] = collections.Counter()
    for commit in commits:
        if len(commit.get('parents', [])) > 1:
            continue
        for file in commit.get('files', []):
            language = language_for_path(file['filename'])
            if language:
                counts[language] += 1
    return dict(counts.most_common())


def main() -> None:
    import subprocess
    from datetime import datetime, timezone
    records = json.loads((ROOT/'data/private_inventory.json').read_text(encoding='utf-8'))
    details: list[dict[str, Any]] = []
    repositories = 0
    for record in records:
        if record['repository'] == f'{ACCOUNT}/{ACCOUNT}':
            continue
        if not (record['owner'] == ACCOUNT or record.get('authored_commit_count_accessible_branches', record.get('authored_commit_count_default_and_accessible_branches', 0))):
            continue
        seen: set[str] = set()
        for branch in record['branches']:
            for commit in gh_list(f"repos/{record['repository']}/commits?sha={quote(branch,safe='')}&author={ACCOUNT}&per_page=100"):
                seen.add(commit['sha'])
        for sha in seen:
            command = subprocess.run(['gh','api',f"repos/{record['repository']}/commits/{sha}"],capture_output=True,text=True,timeout=30,check=False)
            if command.returncode:
                raise RuntimeError('GitHub commit detail request failed')
            details.append(json.loads(command.stdout))
        repositories += 1
    snapshot = {
        'schemaVersion':1,
        'auditDate':datetime.now(timezone.utc).date().isoformat(),
        'measurement':'Source-file touches in authored non-merge commits observed on accessible branches; a file touched in two commits counts twice. This does not measure code ownership, skill or repository language bytes.',
        'repositoriesAnalyzed':repositories,
        'commitsAnalyzed':sum(len(c.get('parents',[])) <= 1 for c in details),
        'commitDetailsUnavailable':0,
        'languages':aggregate_file_touches(details),
    }
    (ROOT/'data/languages.json').write_text(json.dumps(snapshot,indent=2)+'\n',encoding='utf-8')
    print('Public-safe language aggregate updated. Review before committing.')


if __name__=='__main__':
    main()
