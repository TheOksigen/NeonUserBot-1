# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Neon UserBor --------TheOksigen

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.cmdhelp import CmdHelp
import flag
import pytz
from requests import get
from userbot.events import register
from userbot.language import get_value
LANG = get_value("covid19")

# ████████████████████████████████ #


@register(outgoing=True, pattern="^.covid ?(.*)$")
@register(outgoing=True, pattern="^.korona ?(.*)$")
async def covid(event):
    try:
        if event.pattern_match.group(1) == '':
            country = 'AZ'
        else:
            country = event.pattern_match.group(1)

        bayrak = flag.flag(country)
        worldData = get('https://coronavirus-19-api.herokuapp.com/all').json()
        countryData = get(
            'https://coronavirus-19-api.herokuapp.com/countries/' +
            pytz.country_names[country]).json()
    except BaseException:
        await event.edit(LANG['SOME_ERRORS'])
        return

    sonuclar = (
        f"** {LANG['DATA']}**\n" +
        f"\n**{LANG['EARTH']}**\n" +
        f"**{LANG['CASE']}** `{worldData['cases']}`\n" +
        f"**{LANG['DEATH']}** `{worldData['deaths']}`\n" +
        f"**{LANG['HEAL']}** `{worldData['recovered']}`\n" +
        f"\n**{pytz.country_names[country]}**\n" +
        f"**{bayrak} {LANG['AZ_ALL_CASES']}** `{countryData['cases']}`\n" +
        f"**{bayrak} {LANG['AZ_CASES']}** `{countryData['todayCases']}`\n" +
        f"**{bayrak} {LANG['AZ_CASE']}** `{countryData['active']}`\n" +
        f"**{bayrak} {LANG['AZ_ALL_DEATHS']}** `{countryData['deaths']}`\n" +
        f"**{bayrak} {LANG['AZ_DEATHS']}** `{countryData['todayDeaths']}`\n" +
        f"**{bayrak} {LANG['AZ_HEAL']}** `{countryData['recovered']}`\n" +
        f"**{bayrak} Test Sayısı:** `{countryData['totalTests']}`")
    await event.edit(sonuclar)

CmdHelp('covid19').add_command(
    'covid',
    '<ülke kodu>',
    'Həm dünyada, həm də təqdim etdiyiniz ölkə üçün mövcud Covid 19 statistikası. Ölkəniz fərqlidirsə, onu əmrin yanına əlavə edin.',
    'covid az -> Azerbaycanı getirir.').add_warning('`Ölkə yazmasaz Azerbaycanı secər.`').add()
