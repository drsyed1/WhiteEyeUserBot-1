import secrets

from WhiteEyeUserBot import sclient
from WhiteEyeUserBot.utils import WhiteEye_on_cmd

"""This Is Only For Devs Of AntispamInc, Needs Root Permissions // @AntispamInc"""


@WhiteEye.on(WhiteEye_on_cmd(pattern="benheck(?: |$)(.*)"))
async def oki(event):
    await event.edit("`Processing...`")
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        userz = args[0]
        if userz.isnumeric():
            user = int(userz)
        else:
            await event.edit("Provide User-ID Not Username.")
            return
        if len(args) == 2:
            extra = args[1]
        if extra == None:
            await event.edit("Reason Can't Be None")
            return
        elif extra == "":
            await event.edit("Reason Can't Be None")
            return
        if not user:
            await event.edit("Reply To User Or Mention a User.")
            return
    gensys = sclient.ban(user, extra)
    await borg.send_message("antispamincfed", f"/fban {user} {extra}")
    if gensys["error"] == True:
        await event.edit("Error : " + gensys["full"])
    else:
        await event.edit(
            f"**User :** `{user}` \n**Reason :** `{extra}` \n**Banned Sucessfully !**"
        )


@WhiteEye.on(WhiteEye_on_cmd(pattern="heck(?: |$)(.*)"))
async def oka(event):
    await event.edit("`Processing...`")
    args = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user = await event.client.get_entity(previous_message.sender_id)
    elif args:
        userz = args
        if userz.isnumeric():
            user = int(userz)
        else:
            await event.edit("Fuck, Gib ID")
            return
        if not user:
            await event.edit("Reply To User Or Mention a User.")
            return
    gensys2 = sclient.unban(user)
    await borg.send_message("antispamincfed", f"/unfban {user}")
    if gensys2["error"] == True:
        await event.edit("Error : " + gensys2["full"])
    else:
        await event.edit(f"**User :** `{user}` \n**UnBanned Sucessfully !**")


@WhiteEye.on(WhiteEye_on_cmd(pattern="nt"))
async def tokens(event):
    await event.edit("`Processing...`")
    okbabe = secrets.token_urlsafe(16)
    skynet = sclient.new_token(okbabe)
    if skynet["error"] == True:
        await event.edit("Error : " + gensys2["full"])
    else:
        await event.edit(f"**New Token** \n**Token** : `{okbabe}`")
