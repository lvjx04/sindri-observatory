# Sindri Operator Observatory

Interactive preview of an operator catalog, benchmark comparisons, case history, and profiler views.

## Preview data

The page uses demonstration measurements and browser-local state. API metadata is a snapshot from November 18, 2026. Case edits and simulated jobs are stored in the current browser.

## Run locally

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Open http://127.0.0.1:8080. The standalone `index.html` includes the application, styles, and demo dataset.

## Deployment

Serve `index.html` with a static HTTP server. This repository holds the initial preview exported from the existing design prototype.
