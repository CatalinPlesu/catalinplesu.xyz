#!/bin/python

from flask import Flask, render_template, url_for, redirect
from markupsafe import escape

app = Flask(__name__)

singl = {
    "links": {
        "Github": "https://github.com/CatalinPlesu",
        "Gitlab": "https://gitlab.com/catalinplesu",
        "Telegram": "https://t.me/catalinplesu",
        "Reddit": "https://www.reddit.com/user/_katarin",
        "Twitter": "https://twitter.com/catalinplesu",
        "YouTube": "https://www.youtube.com/channel/UC752pTuCebS37pCYwYPirow",
        "LinkedIn": "https://www.linkedin.com/in/c%C4%83t%C4%83lin-ple%C8%99u-042872209/",
        "Resume": "static/Catalin_Plesu_Resume.pdf",
        "Oroboros": "https://oroboros.app",
    },

    "profile": {
        "avatar": "avatar2.jpg",
        "author": "Cătălin Pleșu",
        "description_url": "Pseudo Human, under continuous development.",
        "description": """Elixir Enthusiast ⚡ |> Full-stack Engineer |> Creating Oroboros
        Gruvbox ♥️""",
    },

    "navbar_left": ["Home"],
    "navbar_right": ["Contact", "About"],
}


@app.route('/')
def home():
    return render_template('index.html', singl=singl)


@app.route('/contact')
def contact():
    return render_template('contact.html', singl=singl)


@app.route('/about')
def about():
    return render_template('about.html', singl=singl)


@app.route('/<item>')
def telegram(item):
    for key in singl["links"]:
        if item.lower() == key.lower():
            return redirect(singl["links"][key])
    return f"No such redirect '<b>{item}</b>'"
