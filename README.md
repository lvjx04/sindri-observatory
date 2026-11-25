# Sindri Operator Observatory

Interactive preview of an operator catalog, benchmark comparisons, case history, and profiler views.

[Open the live preview](http://8.161.214.41/)

## Preview data

The page uses demonstration measurements and browser-local state. API metadata is a snapshot from November 18, 2026. Case edits and simulated jobs are stored in the current browser.

## Run locally

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Open http://127.0.0.1:8080. `index.html` includes the original application and demo dataset. The runner status bar loads `data/runner-demo.json` every 15 seconds.

## Deployment

The **Deploy Observatory** workflow publishes `main` after pushes and manual dispatches. It runs on the repository-scoped `ecs01-observatory` runner, with the `observatory` label.

The ECS preview uses Nginx with `deploy/nginx.conf`. `scripts/deploy.py` writes a complete snapshot under `/var/www/sindri-observatory/releases`, then switches the `current` symlink used by Nginx. `deployment.json` records the published commit and workflow run. Nginx runs as a systemd service with automatic startup.

## Runner update demo

Run **Actions → Simulate runner update → Run workflow** on `main`. The workflow creates a timestamped demo record, commits it as `github-actions[bot]`, and explicitly dispatches deployment. An open page picks up the new record on its next 15-second check.

GitHub suppresses push-triggered workflows for commits pushed with `GITHUB_TOKEN`. The simulation therefore uses `workflow_dispatch` to start deployment after the push. Its token has `contents: write` and `actions: write`; the deployment workflow uses `contents: read`.
