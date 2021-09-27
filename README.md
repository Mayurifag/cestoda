# Cestoda

## Description

Cestoda is Telegram userbot made with Python with some cool features to make
your own awesome feed channel via posts from other tg channels.

Imagine you have 100 channels on your 2nd telegram account and you're unable to
read them. You just create «feed» channel, get its chat_id and now you are fine.
You would have content from all these channels:

* Without ads and content you dont like (see `CHAT_WORDS_TO_FILTER` below)
* Messages would be already «read» by Cestoda in these channels, so you wont
have these dumb notifications and red/gray badge on tg icon

## Configuration & launch

You need to setup bot via ENV, so lets make `.env` file for dev purposes:

```sh
# get id/hash from my.telegram.org/
API_ID=xxx
API_HASH=xxx
PHONE_NUMBER=+77777777777
SESSION_NAME=cestoda
CHAT_NAMES_FOR_FEED=general_it_talks/dmitriyrozhkov/daily_rozhok
CHAT_WORDS_TO_FILTER=реклама
FEED_CHAT_ID=-10012312321

```

Install requirements: `pip3 install -r requirements.txt`
Launch bot: `python3 core.py`

## Ongoing

I wish to make bot way more better creature; have clean code, have docker, use
modular architecture, make application, etc. But I still pushed it to github to
have something like proof-of-working shitcode implementation. Don't blame me.
