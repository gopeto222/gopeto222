# Activity metric method

`scripts/metrics.py` requests GitHub's `contributionsCollection.contributionCalendar` for the profile account. The yearly total and active day count come directly from that calendar. Streaks are calculated from consecutive days with a positive contribution count. The current streak may end yesterday to account for the ongoing day. The card records its UTC generation date.

The public calendar can include private contributions according to the account's GitHub settings, but this repository stores only daily counts and does not publish private repository names or source. Calendar contributions are not equivalent to commits, code volume, hours, or ownership of an organization repository. The graphic deliberately omits language shares and repository counts because GitHub repository language bytes cannot be assigned fairly to an individual collaborator.

The scheduled workflow uses the repository `GITHUB_TOKEN` for a read-only GraphQL query. It commits changed generated assets with temporary `contents: write` permission. The normal test job uses read-only permission.
