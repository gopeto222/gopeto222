"""Authenticated repository audit. Writes private evidence only to ignored storage.

Run locally with an authenticated GitHub CLI: python3 scripts/discovery.py
The generated private inventory must never be committed or copied into a public asset.
"""
from __future__ import annotations

import json
import subprocess
import urllib.parse
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ACCOUNT = 'gopeto222'


def gh_list(path: str) -> list[dict[str, Any]]:
    process = subprocess.run(['gh', 'api', '--paginate', path, '--jq', '.[]'], capture_output=True, text=True, timeout=90, check=False)
    if process.returncode:
        raise RuntimeError(f'GitHub API request failed for {path}: {process.stderr.strip()}')
    return [json.loads(line) for line in process.stdout.splitlines() if line.strip()]


def contribution_evidence(owner: str, author_commits: int, authored_prs: int) -> bool:
    return owner == ACCOUNT or author_commits > 0 or authored_prs > 0


def public_record_is_safe(record: dict[str, Any]) -> bool:
    return record.get('visibility') != 'private' or record.get('repository') is None


def audit() -> list[dict[str, Any]]:
    repos = gh_list('user/repos?per_page=100&affiliation=owner,collaborator,organization_member')
    result=[]
    for repo in repos:
        full = repo['full_name']
        branches = gh_list(f'repos/{full}/branches?per_page=100')
        shas: set[str] = set()
        for branch in branches:
            encoded = urllib.parse.quote(branch['name'], safe='')
            shas.update(commit['sha'] for commit in gh_list(f'repos/{full}/commits?sha={encoded}&author={ACCOUNT}&per_page=100'))
        prs = gh_list(f'repos/{full}/pulls?state=all&per_page=100')
        mine = [pr['number'] for pr in prs if pr.get('user', {}).get('login') == ACCOUNT]
        result.append({
            'repository': full,
            'owner': repo['owner']['login'],
            'organization': repo['owner']['login'] if repo['owner']['type'] == 'Organization' else None,
            'visibility': 'private' if repo['private'] else 'public',
            'archived': repo['archived'],
            'description': repo.get('description'),
            'last_activity': repo.get('pushed_at'),
            'authored_commit_count_accessible_branches': len(shas),
            'authored_commit_samples': sorted(shas)[:3],
            'branches': [branch['name'] for branch in branches],
            'authored_pull_requests': mine,
            'included': contribution_evidence(repo['owner']['login'], len(shas), len(mine)),
        })
    return result


def main() -> None:
    output = ROOT/'data/private_inventory.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(audit(), indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Private audit saved locally: {output}. Do not commit this file.')


if __name__ == '__main__':
    main()
