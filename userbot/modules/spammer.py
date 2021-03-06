# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# NEON USER BOT


import asyncio
import threading

from userbot import BOTLOG, BOTLOG_CHATID
from userbot.events import register
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern="^.tspam")
async def tmeme(e):
    message = e.text
    messageSplit = message.split(" ", 1)
    tspam = str(messageSplit[1])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID,
            "#TSPAM \n\n"
            "TSpam uğurla gerçəkləşdi."
        )


@register(outgoing=True, pattern="^.spam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit = message.split(" ", 2)
        counter = int(messageSplit[1])
        spam_message = str(messageSplit[2])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#SPAM \n\n"
                "Spam uğurla gerçəkləşdi."
            )


@register(outgoing=True, pattern="^.bigspam")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit = message.split(" ", 2)
        counter = int(messageSplit[1])
        spam_message = str(messageSplit[2])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#BIGSPAM \n\n"
                "Bigspam uğurl gerçəkləşdi."
            )


@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        link = str(text[2])
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, link)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#PICSPAM \n\n"
                "PicSpam uğurla gerçəkləşdi."
            )


@register(outgoing=True, pattern="^.delayspam")
async def delayspammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit = message.split(" ", 3)
        spam_delay = float(messageSplit[1])
        counter = int(messageSplit[2])
        spam_message = str(messageSplit[3])
        await e.delete()
        delaySpamEvent = threading.Event()
        for i in range(1, counter):
            await e.respond(spam_message)
            delaySpamEvent.wait(spam_delay)
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#DelaySPAM \n\n"
                "DelaySpam uğurla gerçəkləşdi."
            )

CmdHelp('spammer').add_command(
    'tspam', '<mətn>', 'Verilən mesajı tək tək göndərərək spam edər.'
).add_command(
    'spam', '<miqdar> <mətn>', 'Verilen miqdarda spam göndərər.'
).add_command(
    'bigspam', '<miqdar> <mətn>', 'Verilən miqdarda spam göndərər.'
).add_command(
    'picspam', '<miqdar> <link>', 'Verilən miqdarda şəkilli spam göndərər.'
).add_command(
    'delayspam', '<gecikmə> <miqdar> <mətn>', 'Verilən miqdar və verilən gecikmə ilə gecikməli spam edər.'
).add_warning(
    'Diqqət Siz Spam həyata keçirərkən hesabınızın limitə düşmə riskini gözə alırsınız bundan NEON User Bot komandası məsuliyət daşımır!!'
).add()
