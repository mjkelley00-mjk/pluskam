# +kam website (pluskam.com)

A static rebuild of the +kam site, ready to host for free on GitHub Pages.
Plain HTML/CSS — no build step, no dependencies, nothing to pay for.

## Files

| File | Page |
|------|------|
| `index.html` | Work (home) |
| `services.html` | Services |
| `casestudies.html` | Case Studies overview |
| `casestudies-gogosqueez.html` | Case study — GoGo Squeez |
| `casestudies-v8vfusion.html` | Case study — V8 V-Fusion+Energy |
| `casestudies-networkperformance.html` | Case study — Zoom Active Lifestyle Marketing |
| `casestudies-orbit5gum.html` | Case study — Orbit / 5 Gum |
| `about.html` | About |
| `contact.html` | Contact |
| `css/style.css` | All styling |
| `CNAME` | Custom domain for GitHub Pages |
| `sitemap.xml` | Sitemap for search engines |
| `localize_images.py` | Optional: pull images off Wix into this repo |

## Publish to GitHub Pages

1. Create a new repository on GitHub (e.g. `pluskam-site`).
2. Upload every file here, keeping the folder structure (the `css/` folder must stay a folder). You can drag-and-drop into GitHub's web uploader, or use git:
   ```
   git init
   git add .
   git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/<you>/pluskam-site.git
   git push -u origin main
   ```
3. In the repo, go to **Settings → Pages**.
4. Under **Build and deployment**, set **Source = Deploy from a branch**, **Branch = main**, folder **/ (root)**, and Save.
5. Wait ~1 minute. Your site appears at `https://<you>.github.io/pluskam-site/`.

## Point pluskam.com at GitHub Pages

The included `CNAME` file already sets the domain to `www.pluskam.com`.

At your **domain registrar** (where you bought pluskam.com), set DNS:

- A **CNAME** record: host `www` → value `<you>.github.io`
- For the bare domain `pluskam.com`, four **A** records pointing to GitHub:
  `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`

Then in **Settings → Pages → Custom domain**, enter `www.pluskam.com`, save, and tick **Enforce HTTPS** once it's available.

> If your domain is currently managed by Wix, you'll change these DNS records in the Wix domain settings (or move the domain to another registrar). Do this only once GitHub Pages is live so the site never goes dark.

## Turn on the contact form

The form uses [Formspree](https://formspree.io) (free tier). To activate it:

1. Sign up at formspree.io and create a form.
2. Copy the form ID it gives you (looks like `xyzabcd`).
3. In `contact.html`, replace `YOUR_FORM_ID` in this line:
   ```html
   <form class="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
   Submissions will be emailed to the address on your Formspree account.

Until then, the office address, email, and phone on the Contact page all work.

## Optional: host images in the repo instead of on Wix

Right now images load from Wix's CDN (`static.wixstatic.com`). That works, but
if you ever want the site fully self-contained, run:

```
python localize_images.py
```

This downloads every image into `images/` and rewrites the HTML to use those
local copies. Commit the new files and push. (Requires Python 3. Run it on your
own computer — it needs internet access to Wix.)

## Editing content

Everything is plain text. Open any `.html` file, change the words, save, and
push. Styling lives entirely in `css/style.css`.
