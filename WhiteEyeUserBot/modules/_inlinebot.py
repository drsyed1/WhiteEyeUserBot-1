import asyncio
import os
import re
from math import ceil

from telethon import Button, custom, events, functions

from WhiteEyeUserBot import ALIVE_NAME, CMD_HELP, CMD_LIST
from WhiteEyeUserBot.modules import inlinestats

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/63d2f8bcdae4da2ec5e7e.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
LOG_CHAT = Config.PRIVATE_GROUP_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "WhiteEye"
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("WhiteEye"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© WhiteEye Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        if event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Showing Stats For {DEFAULTUSER}'s WhiteEye** \nNote --> Only Owner Can Check This \n(C) @Whiteeyeot",
                buttons=[
                    [custom.Button.inline("Show Stats ", data="terminator")],
                    [
                        Button.url(
                            "Repo 🇮🇳", "https://github.com/WhiteEye-Org/WhiteEyeUserBot"
                        )
                    ],
                    [Button.url("Join Channel ⚓", "t.me/WhiteEyeOT")],
                ],
            )
        if event.query.user_id == bot.uid and query.startswith("**Hello"):
            result = builder.photo(
                file=WARN_PIC,
                text=query,
                buttons=[
                    [
                        custom.Button.inline("❌ Spamming", data="wannaspam"),
                        custom.Button.inline("📝 Chatting", data="casualbitching"),
                    ],
                    [
                        custom.Button.inline("❓ Doubt", data="askme"),
                        custom.Button.inline("🛑 Others", data="others"),
                    ],
                ],
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_popp_up_alert = (
                "Please get your own WhiteEyeUserbot, and don't use mine!"
            )
            await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit(
                "Menu Closed!!",
            )
        else:
            reply_pop_up_alert = "Please get your own WhiteEyeuserbot from @WhiteEyeOT "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Please get your own WhiteEyeUserbot, and don't use mine!"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if not event.query.user_id == bot.uid:
        sedok = "Who The Fuck Are You? Get Your Own WhiteEye."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    plugin_name = event.data_match.group(1).decode("UTF-8")
    if plugin_name in CMD_HELP:
        help_string = f"**💡 PLUGIN NAME 💡 :** `{plugin_name}` \n{CMD_HELP[plugin_name]}"
    reply_pop_up_alert = help_string
    reply_pop_up_alert += "\n\n**(C) @WhiteEyeOT** ".format(plugin_name)
    if len(reply_pop_up_alert) >= 4096:
        crackexy = "`Pasting Your Help Menu.`"
        await event.answer(crackexy, cache_time=0, alert=True)
        out_file = reply_pop_up_alert
        url = "https://del.dog/documents"
        r = requests.post(url, data=out_file.encode("UTF-8")).json()
        url = f"https://del.dog/{r['key']}"
        await event.edit(
            f"Pasted {plugin_name} to {url}",
            link_preview=False,
            buttons=[[custom.Button.inline("Go Back", data="backme")]],
        )
    else:
        await event.edit(
            message=reply_pop_up_alert,
            buttons=[[custom.Button.inline("Go Back", data="backme")]],
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            text = inlinestats
            await event.answer(text, alert=True)
        else:
            txt = "You Can't View My Masters Stats"
            await event.answer(txt, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"wannaspam")))
    async def rip(event):
        await event.get_chat()
        text1 = "You Have Chosed A Probhited Option. Therefore, You Have Been Blocked By WhiteEye. 💢"
        await event.edit("Choice Not Accepted ❌")
        await borg.send_message(event.query.user_id, text1)
        await borg(functions.contacts.BlockRequest(event.query.user_id))

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"casualbitching")))
    async def rip(event):
        await event.get_chat()
        him_id = event.query.user_id
        await event.edit("Choice Accepted ✔️")
        text2 = "Ok. Please Wait Until My Master Approves. Don't Spam Or Try Anything Stupid. \nThank You For Contacting Me."
        await borg.send_message(event.query.user_id, text2)
        await tgbot.send_message(
            LOG_CHAT,
            message=f"Hello, A [New User](tg://user?id={him_id}). Wants To Talk With You.",
            buttons=[Button.url("Contact Him", f"tg://user?id={him_id}")],
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
    async def rip(event):
        await event.get_chat()
        await event.edit("Choice Accepted ✔️")
        text3 = "Ok, Wait. You can Ask After Master Approves You. Kindly, Wait."
        await borg.send_message(event.query.user_id, text3)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"others")))
    async def rip(event):
        await event.get_chat()
        await event.edit("Choice Accepted ✔️")
        text4 = "Ok, Wait. You can Ask After Master Approves You. Kindly, Wait."
        await borg.send_message(event.query.user_id, text4)


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 10
    number_of_cols = 2
    helpable_modules = []
    for p in loaded_modules:
        if not p.startswith("_"):
            helpable_modules.append(p)
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format("⚓", x, "⚓"), data="us_plugin_{}".format(x)
        )
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "Previous", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("❌Close", data="close"),
                custom.Button.inline(
                    "Next", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs
