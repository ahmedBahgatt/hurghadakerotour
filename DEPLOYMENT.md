# Deployment

Static site deployed to **GitHub Pages** via the official GitHub Actions Pages
pipeline, served on the custom domain **hurghadakerotour.com** over HTTPS.

- Repository: <https://github.com/ahmedBahgatt/hurghadakerotour>
- Production URL: <https://hurghadakerotour.com>
- Build output: `dist/` (from `python3 build.py`)
- Pages URL (redirects to the custom domain): <https://ahmedbahgatt.github.io/hurghadakerotour/>

## How the pipeline works

`.github/workflows/deploy.yml` runs two jobs on every push to `main`:

1. **build** - checkout, setup Python 3.12, `scripts/secret-scan.sh`,
   `python3 build.py`, `python3 scripts/check.py` (HTML validity, one H1,
   canonical, no stale domains, valid JSON-LD, sitemap/robots/.nojekyll present),
   then uploads `dist/` as the Pages artifact.
2. **deploy** - `actions/deploy-pages@v4` publishes the artifact.

Triggers: push to `main`, manual `workflow_dispatch`, and
`repository_dispatch` type `sanity-publish` (for a future CMS webhook).

## DNS - set these at Hostinger (hPanel -> Domains -> hurghadakerotour.com -> DNS)

Make sure the domain uses **Hostinger's nameservers** (not "parked"/redirect),
then add these records (remove any conflicting `@` A/AAAA first):

Apex `@` -> A records (all four):
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```
Apex `@` -> AAAA records (optional, IPv6):
```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```
`www` -> CNAME -> `ahmedbahgatt.github.io`

TTL: default. Propagation: minutes to a few hours.

## Custom domain + HTTPS

- The custom domain `hurghadakerotour.com` is already set in the repo's Pages
  settings (no CNAME file needed; GitHub serves it).
- Once DNS resolves, GitHub Settings -> Pages shows "DNS check successful" and
  automatically provisions a Let's Encrypt certificate for the apex and `www`.
- After the certificate is issued, enable **Enforce HTTPS** (Settings -> Pages),
  or run: `gh api -X PUT repos/ahmedBahgatt/hurghadakerotour/pages -F https_enforced=true`
- Recommended: add `hurghadakerotour.com` under GitHub -> Settings -> Pages ->
  "Verified domains" to prevent domain takeover.

## Security practices

- HTTPS enforced by GitHub Pages (HSTS applied by GitHub on the apex).
- Per-page meta: Content-Security-Policy, Referrer-Policy, robots.
- CI gates: secret scan + QA check must pass before deploy.
- Note: GitHub Pages cannot send custom HTTP response headers. For response-level
  CSP/HSTS/X-Frame-Options, front the site with Cloudflare (proxy) later.

## Verifying a deployment

1. Actions tab -> latest "Build and Deploy to GitHub Pages" is green.
2. `curl -I https://hurghadakerotour.com` returns 200 and `https`.
3. Spot-check `/fr/`, `/pl/`, `/ro/` and a tour page; click a WhatsApp button.

## Rollback

Revert the offending commit on `main` and push; the workflow redeploys the
previous good state. Each deploy is also listed under the Actions "Deploy" job.

## Sanity (future CMS)

The content lives in `data/tours.py` + `data/i18n.py`, cleanly separated from
rendering, so it can be ported to Sanity schemas later. The pipeline already
accepts a `CONTENT_SOURCE` repo Variable and a `sanity-publish`
`repository_dispatch` trigger; wiring a Sanity source is a follow-up (schemas +
a fetch layer in `build.py`), not a rewrite.

## Moving to another host later

Any static host works - deploy the `dist/` folder. Only `SITE_URL` in
`site_config.py` (canonical/hreflang/sitemap) needs to match the final domain.
