# Render Deployment Guide

This guide deploys only the Flask chat app (`app.py`) to Render, assuming you already built `chroma_db/` locally.

## 1) Prepare repository contents

Before deploying, ensure these are committed and pushed:

- `app.py`
- `templates/`
- `static/`
- `chroma_db/` (prebuilt locally)
- `render.yaml`
- `requirements.render.txt`

## 2) Build ChromaDB locally (one-time or when docs change)

From your local machine:

```bash
conda activate mast
python ingest.py
```

This populates `./chroma_db`.

## 3) Create Render Web Service

1. Push your branch to GitHub.
2. In Render, choose **New +** → **Web Service**.
3. Connect this repository.
4. Render will read `render.yaml` automatically.

## 4) Required environment variables in Render

Set these in Render service settings:

- `GOOGLE_API_KEY` = your Gemini API key
- `public_password` = shared password users must enter before app access
- `FLASK_SECRET_KEY` = secure random value (or let Render generate from `render.yaml`)

Optional API key aliases are also supported by the app:

- `GEMINI_API_KEY`
- `GOOGLE_GENAI_API_KEY`
- `API_KEY`

## 5) Deploy

Click **Deploy** (or trigger a redeploy after setting env vars).

Expected behavior:

- `/` redirects to `/login` until password is provided.
- After login, chat UI is accessible.
- `/chat` and `/api/config` require authenticated session.

## 6) Update flow

When your source docs change:

1. Re-run `python ingest.py` locally.
2. Commit updated `chroma_db/`.
3. Push and redeploy on Render.

## Troubleshooting

- If app says vector store is not initialized: confirm `chroma_db/` is present in deployed repo and contains data.
- If every answer is fallback only: verify `mast_docs` collection is populated and API key is valid.
- If login fails for everyone: verify `public_password` is set in Render env vars.
