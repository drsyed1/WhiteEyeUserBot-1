"""Emoji
Available Commands:
.deploy"""


import asyncio

from WhiteEyeUserBot import ALIVE_NAME, CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "unknown"


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"deploy"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

    # input_str = event.pattern_match.group(1)

    await event.edit("Deploying...")

    animation_chars = [
        "**Heroku Connecting To Latest Github Build (MrDayamZaidi/WhiteEyeUserBot)**",
        "**Build started by user** **{DEFAULTUSER}**",
        "**Deploy** `535a74f0` **by user** **{MY BOSS}**",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m WhiteEyeUserBot`",
        "**State changed from starting to up**",
        "__INFO:WhiteEyeUserBot:Logged in as 557667062__",
        "__INFO:WhiteEyeUserBot:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])


CMD_HELP.update({"deploy": ".deploy" "\nUsage show fake animation of deploy "})
