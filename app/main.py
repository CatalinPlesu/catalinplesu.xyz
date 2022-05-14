#!/bin/python

from flask import Flask, render_template, url_for, redirect
from markupsafe import escape

app = Flask(__name__)

links = {
    "Github": "https://github.com/CatalinPlesu", "Gitlab": "https://gitlab.com/catalinplesu",
    "Telegram": "https://t.me/catalinplesu",
    "Reddit": "https://www.reddit.com/user/_katarin",
    "Twitter": "https://twitter.com/catalinplesu",
    "Mastodon": "https://linuxrocks.online/@catalin",
    "YouTube": "https://www.youtube.com/channel/UC752pTuCebS37pCYwYPirow",
    "LinkedIn": "https://www.linkedin.com/in/c%C4%83t%C4%83lin-ple%C8%99u-042872209/",
    "Resume": "static/Catalin_Plesu_Resume.pdf",
    "Eden": "https://github.com/catalinplesu/eden",
    "BookMall": "https://github.com/catalinplesu/bookmall",
}

profile = {
    "avatar": "avatar2.jpg",
    "author": "Cătălin Pleșu",
    "description_url": "Pseudo Human, maybe more probably less.",
    "description": "IT Student | Linux User | Anime Enjoyer | Rustacean",
}


@app.route('/')
def home():
    return render_template('index.html', links=links, profile=profile)

@app.route('/<item>')
def telegram(item):
    for key in links:
        if item.lower() == key.lower():
            return redirect(links[key])
    return f"No such redirect '<b>{item}</b>'"
