from resources.cc_alogo import CreditCard
from WhiteEyeUserBot.utils import WhiteEye_on_cmd


@WhiteEye.on(WhiteEye_on_cmd(pattern="cccheck (.*)"))
async def lol(event):
    ccn = event.pattern_match.group(1)
    if ccn.isnumeric():
        card_number = int(ccn)
    else:
        event.edit("Card Number Should Be Only Number")
        return
    card = CreditCard.set_card(card_number)
    sed = f"""{card.company}
Card : {card.card_no}
{card.first_check()}
{card.checksum}
{card.validate()}
"""
    await event.edit(sed)
