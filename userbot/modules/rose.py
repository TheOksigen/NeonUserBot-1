# Neon UserBot - TheOksigen

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.cmdhelp import CmdHelp

chat = "@MissRose_bot"


@register(outgoing=True, pattern="^.fstat ?(.*)")
async def fstat(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)
    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + kullanıcı + " " + text_)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + kullanıcı + " " + text_)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + text_)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + text_)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()


@register(outgoing=True, pattern="^.info ?(.*)")
async def info(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)

    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()


@register(outgoing=True, pattern="^.fedinfo ?(.*)")
async def fedinfo(event):
    if event.fwd_from:
        return
    text_ = event.pattern_match.group(1)
    if text_ == "" and not event.reply_to_msg_id:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo")
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo")
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo " + text_)
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo")
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()


@register(outgoing=True, pattern="^.myfeds ?(.*)")
async def myfeds(event):
    if event.fwd_from:
        return
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/myfeds")
            myfed = await conv.get_response()
            if "file" in myfed.text:
                await myfed.click(0)
                reply = await conv.get_response()
                await event.client.send_message(event.chat_id, reply)
            else:
                await event.client.send_message(event.chat_id, myfed)
                await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("609517172"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/myfeds")
            myfed = await conv.get_response()
            if "file" in myfed.text:
                await myfed.click(0)
                reply = await conv.get_response()
                await event.client.send_message(event.chat_id, reply)
            else:
                await event.client.send_message(event.chat_id, myfed)
                await event.delete()


@register(outgoing=True, pattern="^.fban ?(.*)")
async def fban(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)

    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()


@register(outgoing=True, pattern="^.unfban ?(.*)")
async def unfban(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)

    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()


@register(outgoing=True, pattern="^.feddemote ?(.*)")
async def feddemote(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)

    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/feddemote " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/feddemote " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/feddemode " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()


@register(outgoing=True, pattern="^.fpromote ?(.*)")
async def fpromode(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)

    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fpromote " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fpromote " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fpromote " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fpromote " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()

CmdHelp('rose').add_command(
    'fstat', '<tag/id>', 'Sadəcə .rfstat yazsanız sizin fstat siyahınızı yönləndirər. \n ID və ya istifafəçi adı yazsanız o istifadəçinin fban siyahısını göstərər. '
).add_command(
    'info', '<tag/id>', 'Sadəcə .rinfo yazsanız özünüz üçün məlumat verər. \n ID və ya istifadəçi adı yazsanız o istifadəçi üçün məlumat verər.'
).add_command(
    'fedinfo', '<fed id>', 'Sadəcə .rfedinfo yazsanız sizin Federasiyanız üçün məlumat verər. \n FED ID yazsanız o federasiyanın məlumatını verər.'
).add_command(
    'myfeds', 'Hansı federasyonlarda adminliyiniz olduğunu göstərər..'
).add_command(
    'fban', '<tag/id>', 'Bunu federasiya sahibləri işlədə bilər.\n Qrupdakı birinə öz federasiyanızdan fban ata bilərsiniz. '
).add_command(
    'unfban', '<tag/id>', ' Bunu federasiya sahibləri işlədə bilər.\n Qrupdakı birinə öz federasiyanızda olan fban-ı aça bilərsiniz. '
).add_command(
    'fpromote', '<tag/id>', ' Bunu federasiya sahibləri işlədə bilər.\n Qrupdakı birinə öz federasiyanızda icazə verə bilərsiniz. '
).add_command(
    'feddemote', '<tag/id>', ' Bunu federasiya sahibləri işlədə bilər.\n Qrupdakı birindən öz federasiyanızda olan yetkisini ala bilərsiniz. '

).add()
