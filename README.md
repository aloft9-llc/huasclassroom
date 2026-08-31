# Hua's Classroom

Static teaching notes for **Shanghai Maths Grade 3** and **Singapore Intensive Practice 3A**, published at [huasclassroom.com](https://huasclassroom.com).

## Project layout

| Path | Purpose |
|------|---------|
| `web/` | Static site (HTML, CSS, images) — this is what gets deployed |
| `web/assets/css/` | Shared styles (`tokens`, `base`, `home`, `lesson`, …) |
| `Notes/` | Markdown source notes (not deployed) |
| `Input/` | Original workbook photos (not deployed) |
| `.ocr/` | OCR working files (not deployed) |

## 1. Run locally (optional)

The site is **fully static** (HTML, CSS, images in `web/`). There is no server backend.

`npm run serve` is only for previewing on your machine:

```bash
npm run serve
```

Open [http://localhost:3000](http://localhost:3000).

No install step — `serve` is fetched on first run. Alternative: `python3 -m http.server 3000 --directory web`.

## 2. Push to a private GitHub repo

```bash
git init
git add .
git commit -m "Initial commit: Hua's Classroom static site"
gh repo create huasclassroom --private --source=. --remote=origin
git push -u origin main
```

> **Note:** GitHub Pages on a **private** repo requires a paid GitHub plan (Pro or Organization). On the free tier, use a public repo or deploy elsewhere (AWS S3 + CloudFront, Google Cloud Storage, Cloudflare Pages, etc.).

## 3. Deploy to GitHub Pages

The `web/` folder is published as-is — no build step, no Node server.

1. **Enable Pages first** (required before the first deploy):
   - Repo → **Settings → Pages → Build and deployment**
   - Source: **GitHub Actions**
2. Push to `main`, or run **Actions → Deploy to GitHub Pages → Run workflow**
3. The workflow in `.github/workflows/deploy.yml` uploads the `web/` folder.

Live site: [https://huasclassroom.com](https://huasclassroom.com)

### If you see “There isn't a GitHub Pages site here” (404)

Usually Pages was not enabled before the first workflow run. Fix:

1. **Settings → Pages** → set Source to **GitHub Actions**
2. **Actions → Deploy to GitHub Pages → Run workflow**
3. Wait ~1 minute, then open [https://huasclassroom.com](https://huasclassroom.com)

### Custom domain (`huasclassroom.com`)

`web/CNAME` is already set. In **Settings → Pages → Custom domain**, enter `huasclassroom.com` and add the DNS records GitHub shows (typically `A` records to GitHub IPs, or a `CNAME` to `<user>.github.io`). Enable **Enforce HTTPS** once DNS verifies.

## CSS structure

- `tokens.css` — colors, spacing, site URL variable
- `base.css` — typography, top bar, footer
- `home.css` — homepage layout
- `about.css` — about page
- `lesson.css` — all lesson/note pages
- `lesson-s2.css` — Second Semester copper theme override

Lesson pages load `lesson.css` (+ `lesson-s2.css` for S2 and concept guides). Singapore pages use `lesson.css` (navy accents are built in).
