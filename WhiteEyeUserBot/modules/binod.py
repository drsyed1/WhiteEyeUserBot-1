from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"bid ?(.*)"))
async def bid(event):
    if event.fwd_from:
        return
    giveVar = event.text
    bid = giveVar[4:5]
    if not bid:
        bid = "😂"
    await event.edit(
        f"{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}                     {bid}{bid}\n{bid}{bid}                     {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}                     {bid}{bid}\n{bid}{bid}                     {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n\n{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}\n\n{bid}{bid}                           {bid}{bid}\n{bid}{bid}{bid}                       {bid}{bid}\n{bid}{bid}{bid}{bid}                 {bid}{bid}\n{bid}{bid}  {bid}{bid}               {bid}{bid}\n{bid}{bid}     {bid}{bid}            {bid}{bid}\n{bid}{bid}         {bid}{bid}        {bid}{bid}\n{bid}{bid}             {bid}{bid}    {bid}{bid}\n{bid}{bid}                 {bid}{bid}{bid}{bid}\n{bid}{bid}                     {bid}{bid}{bid}\n{bid}{bid}                          {bid}{bid}\n\n           {bid}{bid}{bid}{bid}{bid}\n     {bid}{bid}{bid}{bid}{bid}{bid}{bid}\n   {bid}{bid}                   {bid}{bid}\n {bid}{bid}                       {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n {bid}{bid}                       {bid}{bid}\n   {bid}{bid}                   {bid}{bid}\n      {bid}{bid}{bid}{bid}{bid}{bid}{bid}\n            {bid}{bid}{bid}{bid}{bid}\n\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}                      {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                      {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}"
    )


CMD_HELP.update({"binod": ".binod\nUse - have funn lol!"})
