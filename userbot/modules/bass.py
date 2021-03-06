# N Σ O N / nusrte / nusr҂e
# Oğurlayanın anasın sikim
# Əkmə peysər
# Var yoxunda olan bütün lifcik taxanları sikim ay peysər
# ƏKMƏ QƏHBƏ BALASI.

# ============================== IMPORTS =================================
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep as t
# ===============================================================================


@register(outgoing=True, pattern="^.bass(?: |$)(.*)")
async def BassBooster(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        input = event.pattern_match.group(1)
    else:
        await event.edit("🔸 __Bass effekti üçün bass səviyyəsi təyin et!__")
        return
    if not event.reply_to_msg_id:
        await event.edit("ℹ️ __Hansı musiqiyə bass vermək lazımdırsa, cavab ver ona.__")
        return
    cavab = await event.get_reply_message()
    if not cavab.media:
        await event.edit("ℹ️ __Hansı musiqiyə bass vermək lazımdırsa, cavab ver ona.__")
        return
    me = await event.client.get_me()
    username = f"@{me.username}" if me.username else my_mention
    chat = "@Baasss_bot"
    await event.edit("__Bass effekti gücləndirilir...__ 🔊")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True,
                                  from_users=488701812
                                  )
            )
            reply = await event.client.send_message(chat, cavab)
            t(3)
            strr = await event.client.send_message(chat,
                                                   input
                                                   )
            response = await response
        except YouBlockedUserError:
            await event.edit(f"**{chat}'u blokdan çıxart və yenidən yoxla.**")
            return
        if response.text.startswith("Forward"):
            await event.edit("Gizlilik ayarlarınızdakı ileti qismini düzəldin.")
        else:
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption="""
<b>🔸 Bass səviyyəsi <a href=\"https://t.me/Neonsup\">N Σ O N</a> ilə gücləndirildi.
🔊 Bass səviyyəsi -</b> <code>{}</code>
🀄️ <b>Mənim Sahibim - {}</b>
""".format(input, username),
                parse_mode="HTML",
                reply_to=cavab)
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.delete_messages(conv.chat_id,
                                               [reply.id,
                                                strr.id,
                                                response.id])

# ------------------------------ CMDHELP ------------------------------------

Kömək = CmdHelp('bass')
Kömək.add_command(
    "bass <Audio faylına cavab>",
    "<Bass səviyyəsi>",
    "Musiqinin bass səviyyəsini çoxaldar.")
Kömək.add_info("**@Nusrets Tərəfindən Yaradılıb.**")
Kömək.add()
