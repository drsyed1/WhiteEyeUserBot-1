# Originally created By KingMars ✅ Rain Sequence 2 {Updated}
import asyncio
from collections import deque

from telethon import events

from WhiteEyeUserBot import CMD_HELP


@WhiteEye.on(events.NewMessage(pattern=r"\.km_rain2", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("☁️⛈Ř/~\İŇ🌬⚡🌪"))
    for _ in range(100):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


CMD_HELP.update(
    {
        "rain": "Rain\
\n\nSyntax : .rain\
\nUsage : Baarish"
    }
)
