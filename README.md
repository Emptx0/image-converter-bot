# Telegram image to PDF/JPG converter bot
This bot can convert your images to one PDF file or JPG images.
## Commands
The bot supports `/start` and `/convert` commands.<br/>
* `/start` - to get welcome message.<br/>
* `/convert` - to convert images that was sent to bot.<br/>
## Required libraries
The bot requires the following Python libraries:
* aiogram
* PIL
## Setup
1) Create new bot in [BotFather](https://t.me/BotFather) using `/newbot` command and get your bot token. Paste it in `main.py` line 14 `token`
2) Using cmd move to project directory and install libraries with following command:<br/>
```
pip install aiogram Pillow
```
3) Run `main.py` with command:
```
python main.py
```
## How the bot works?
This bot will save your images and generated files to a temporary directory.<br/>
After sending result to user temporary directory will be deleted.
