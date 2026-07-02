#!/usr/bin/env python3
"""
localize_images.py  —  make the +kam site fully independent of Wix.

By default the site loads images straight from Wix's CDN
(static.wixstatic.com). That works, but keeps a dependency on Wix.
Run this ONCE to download every image into ./images and rewrite the
HTML so it points at those local files instead.

    python localize_images.py

Requires Python 3 (no extra packages). Safe to re-run.
"""
import os
import re
import sys
import glob
from urllib.request import urlopen, Request

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, "images")

# Wix media file  ->  local filename
MAP = {
    "699c5b_e719340a727a412987a80271787770bd~mv2.png": "logo.png",
    "0fdef751204647a3bbd7eaa2827ed4f9.png": "social-facebook.png",
    "c7d035ba85f6486680c2facedecdcf4d.png": "social-twitter.png",
    "01c3aff52f2a4dffa526d7a9843d46ea.png": "social-instagram.png",
    "5b7e139d046c40c1a1acde7162607721.jpg": "brand-1.jpg",
    "699c5b_2b488449bea849fd999d9112682c3ec6~mv2.png": "brand-2.png",
    "699c5b_da87a55d64cf44cdaf8e06ab1b8a76ef~mv2.png": "brand-3.png",
    "699c5b_936bf2710ff744f5983d1478b7539344~mv2.png": "brand-4.png",
    "699c5b_0b45741aace54163af43c3b71468cc03~mv2.png": "brand-5.png",
    "699c5b_cd55074d0d024cf9aa2cbbce0f26d117~mv2.png": "brand-6.png",
    "699c5b_db91fc25c3364fceaca77214775293a1~mv2_d_2000_1331_s_2.png": "brand-7.png",
    "699c5b_a6496b8225dc4d33bc3aba01829b417e~mv2.png": "brand-8.png",
    "699c5b_7509fdab5a824f33b9537ab2853102f2~mv2.png": "brand-9.png",
    "699c5b_8090ab0aa52e4c168d02d32192342013~mv2_d_4160_2340_s_2.jpg": "services-hero.jpg",
    "699c5b_9c3dd7747ff3429fbc6b404f46b93e02~mv2_d_5312_2988_s_4_2.jpg": "about.jpg",
    "699c5b_cd812999ca7e4c44b8a4f26dc273f17d~mv2_d_6016_4000_s_4_2.jpg": "gogosqueez-1.jpg",
    "699c5b_f3f096ace3a041a49d19e2b3ec77ccce~mv2_d_6016_4000_s_4_2.jpg": "gogosqueez-2.jpg",
    "699c5b_bfe38fa3e8fe428b92d404c56925fff7~mv2_d_6016_4000_s_4_2.jpg": "gogosqueez-3.jpg",
    "699c5b_ef56e2db5eb0497fbf26d33ad5cee51a~mv2_d_4662_2628_s_4_2.jpg": "gogosqueez-4.jpg",
    "699c5b_1783b024e6154355a1ac221944e86b34~mv2_d_2144_2082_s_2.jpg": "v8-1.jpg",
    "699c5b_ada2fdbb7b1d4ff08b168106afe3251f~mv2.jpg": "v8-2.jpg",
    "699c5b_559bbb3c6ec24afb8b603a9d70d84a3a~mv2.jpg": "v8-3.jpg",
    "699c5b_f89d8c0f6a1f4ef0afb6648f962552fe~mv2.jpg": "zoom-1.jpg",
    "699c5b_9de4c77357eb4abba139d617f5c446a2~mv2.jpg": "zoom-2.jpg",
    "699c5b_392a78af94ff4bb5a6d7e1f2dca32924~mv2.jpg": "zoom-3.jpg",
    "699c5b_f577836e83994b00af454604e402824e~mv2.jpg": "zoom-4.jpg",
    "699c5b_b971c66992e9436ea56789c349066186~mv2_d_4000_3000_s_4_2.jpg": "orbit-1.jpg",
    "699c5b_f9e868e645504048877bc13abde82259~mv2_d_1984_1488_s_2.jpg": "orbit-2.jpg",
    "699c5b_b4424e344503415cac742fbd5d5640d3~mv2_d_3222_1944_s_2.jpg": "orbit-3.jpg",
    "699c5b_62534574b42c438e84206c2a93d1cfa4~mv2_d_4000_3000_s_4_2.jpg": "orbit-4.jpg",
}

BASE = "https://static.wixstatic.com/media/"


def download():
    """Returns the set of Wix files that are now present locally."""
    os.makedirs(IMG_DIR, exist_ok=True)
    ok = set()
    for remote, local in MAP.items():
        dest = os.path.join(IMG_DIR, local)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            print(f"  skip  {local} (already here)")
            ok.add(remote)
            continue
        url = BASE + remote
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            data = urlopen(req, timeout=30).read()
            if not data:
                raise ValueError("empty response")
            with open(dest, "wb") as f:
                f.write(data)
            print(f"  saved {local}  ({len(data)//1024} KB)")
            ok.add(remote)
        except Exception as e:
            print(f"  FAIL  {local}: {e}", file=sys.stderr)
    return ok


def rewrite_html(ok):
    """Only swap in local paths for images that actually downloaded."""
    for html in glob.glob(os.path.join(HERE, "*.html")):
        with open(html, "r", encoding="utf-8") as f:
            text = f.read()
        original = text
        for remote, local in MAP.items():
            if remote in ok:
                text = text.replace(BASE + remote, "images/" + local)
        if text != original:
            with open(html, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"  rewrote {os.path.basename(html)}")


if __name__ == "__main__":
    print("Downloading images to ./images ...")
    ok = download()
    total = len(MAP)
    if not ok:
        print(f"\nNo images downloaded ({total} failed). HTML left untouched — "
              "check your internet connection and try again.", file=sys.stderr)
        sys.exit(1)
    print("Rewriting HTML to use the images that downloaded ...")
    rewrite_html(ok)
    if len(ok) < total:
        print(f"\nNote: {total - len(ok)} image(s) failed and were left pointing at Wix. "
              "Re-run this script to retry just those.")
    else:
        print("Done. All images are local now — the site no longer depends on Wix.")
