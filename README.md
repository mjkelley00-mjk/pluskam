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

DNS for pluskam.com is currently hosted at Wix (nameservers `ns10/ns11.wixdns.net`),
so you'll edit these in the Wix **Manage DNS Records** panel. The `CNAME` file in
this repo already sets the site domain to `www.pluskam.com`.

**Change ONLY the two website records:**

| Type | Host | Current value (Wix) | New value |
|------|------|---------------------|-----------|
| A | `pluskam.com` | `185.230.63.171`, `185.230.63.186`, `185.230.63.107` | Replace all three with GitHub's four: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` |
| CNAME | `www.pluskam.com` | `cdn1.wixdns.net` | `<your-username>.github.io` |

**Leave every other record exactly as it is — these run your email and Google
services, and deleting any of them will break email:**

- All **MX** records (Google Workspace mail)
- **TXT** `v=spf1 include:_spf.google.com ~all`
- **CNAME** `calendar`, `docs`, `mail` → `ghs.googlehosted.com`
- **CNAME** `imap`, `pop`, `smtp`, `webmail` → fatcow (email)
- **CNAME** `m.pluskam.com` → wixdns (harmless leftover; optional to remove later)
- **NS** records (not editable)

Then in GitHub **Settings → Pages → Custom domain**, enter `www.pluskam.com`, save,
and tick **Enforce HTTPS** once it becomes available (can take up to an hour).

> **Do this only after the GitHub site looks right at the github.io URL**, so the
> domain never goes dark. And keep the domain/DNS active at Wix — cancel the Wix
> *website plan* if you like, but don't close the whole account or the domain, or
> you'll lose the DNS that your email depends on. To leave Wix entirely, transfer
> the domain to another registrar first and re-create the email records there.

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
