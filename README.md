# json2dart

## _Discord bot to convert JSON code into Dart Class_

[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-tomato.svg?style=flat&logo=git)](https://github.com/parthp-7span/json2dart-discord-bot/issues) [![GitHub stars](https://img.shields.io/github/stars/parthp-7span/json2dart-discord-bot.svg?logo=github)](https://github.com/parthp-7span/json2dart-discord-bot/stargazers) [![GitHub forks](https://img.shields.io/github/forks/parthp-7span/json2dart-discord-bot.svg?logo=github&color=yellow)](https://github.com/parthp-7span/json2dart-discord-bot/network) [![GitHub top language](https://img.shields.io/github/languages/top/parthp-7span/json2dart-discord-bot?color=blue&logo=python)](https://github.com/parthp-7span/json2dart-discord-bot)

## How to use?

Step 1: Invite bot to your discord server using
below <a href="https://discord.com/api/oauth2/authorize?client_id=989037591980564480&permissions=2147519488&scope=bot%20applications.commands">
link.</a>

<p align="center">
<a href="https://discord.com/api/oauth2/authorize?client_id=989037591980564480&permissions=2147519488&scope=bot%20applications.commands">
<img src="./ss/invitebot.png" width="200"/>
</a>
</p>

Step 2: DM your JSON code to `json2dart` bot `or` paste your JSON code to any text channel of your server.

## Use

<img src="./ss/ss1.gif"/>

##  

<img src="./ss/ss2.gif"/>

## Prerequisite
- Python3
- Dart
- [Discord.py](https://discordpy.readthedocs.io/en/stable/)

## Project Setup
1. Clone this repository to your workspace
```shell
git clone https://github.com/parth-p-7span/json2dart-discord-bot.git
```
2. Navigate to json2dart-discord-bot directory in your terminal
```shell
cd json2dart-discord-bot
```
3. Install required packages using below command
```shell
pip install -r requirements.txt
```
4. Create a file called `.env` in the project's root directory, then add your Discord bot token inside with the key `TOKEN`
5. Now run `main.py` file to wake up the bot

## Files Structure
- `class_generator.py` : The primary logic for converting a json object to a Dart class is included in this Python script.
- `main.py` : The code for running the Discord bot and interacting with users is included in this Python script.
