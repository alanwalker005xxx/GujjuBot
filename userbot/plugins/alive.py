"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Yup Sir! I'm Alive ^.^ \nYour Bot Is Running\n\nTelethon Version: 6.9.0\nPython: 3.7.3\n\n`"
                     f"`My Owner`: {DEFAULTUSER}\n"
                     "`Telethon Version: 6.9.0\nPython: 3.7.3\nBot Made By:` @Unknown_Hacker_X\n"
                     "`Database Status: Databases Functioning Normally!\n\nAlways With You, My Master!\n`"
                     "[Ask My Owner To Deploy This UserBot!](https://t.me/Unknown_Hacker_X)")
