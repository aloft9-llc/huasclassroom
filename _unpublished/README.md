# Unpublished site content

Files here are **not deployed** to GitHub Pages. Only `web/` is published.

## About page

| File | Original location |
|------|-------------------|
| `about/about.html` | `web/about.html` |
| `about/about.css` | `web/assets/css/about.css` |

### Restore the About page

```bash
npm run restore-about
```

Then add “About Me” links back to `web/index.html` (top bar and footer) and any lesson nav menus you want.

Preview locally before publishing:

```bash
npm run serve
```

When ready:

```bash
npm run publish
```
