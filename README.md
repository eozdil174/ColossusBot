![PyPI - Python Version](https://img.shields.io/badge/python-3.5%203.6-brightgreen.svg)

### Colossus is a discord bot. It's made for making moderation and basic usage easier.


# How to use it ?
---------------------
You can invite the bot to your server by using [this link](https://discordapp.com/oauth2/authorize?client_id=452689243865612304&scope=bot
)


## What do I need to host this bot on my computer ?
---------------------------------------------------

* You need Python 3.6.5 (the version can change in the future updates). You can get it from [here](https://www.python.org/downloads/release/python-365/)

* You need discord.py libraries. To install the library without full voice support, you can just run the following command:

    ```python3 -m pip install -U discord.py```

    Otherwise to get voice support you should run the following command:

    ```python3 -m pip install -U discord.py[voice]```

    You can visit [this repository](https://github.com/Rapptz/discord.py) for more information about discord.py

* You need SQLite files to run database. You can get it from [here](https://www.sqlite.org/download.html)

## How to host the bot on my computer ?
-----------------------------------------

1. Run botSetup.py and enter the bot settings. The basic commands are available in the script itself
2. After configuring the bot, you can close the botSetup.py by simply typing "exit"
3. Now you can run botMain.py. The bot will be ready after few seconds
