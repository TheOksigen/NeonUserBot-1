# Copyright (C) 2020 by TheOksigen
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# NEON UserBot
from userbot import PATTERNS, CMD_HELP, CMD_HELP_BOT


class CmdHelp:
    """
    NEONUSERBOT
    """

    FILE = ""
    ORIGINAL_FILE = ""
    FILE_AUTHOR = ""
    IS_OFFICIAL = True
    COMMANDS = {}
    PREFIX = PATTERNS[:1]
    WARNING = ""
    INFO = ""

    def __init__(
            self,
            file: str,
            official: bool = True,
            file_name: str = None):
        self.FILE = file
        self.ORIGINAL_FILE = file
        self.IS_OFFICIAL = official
        self.FILE_NAME = file_name if file_name is not None else file + '.py'
        self.COMMANDS = {}
        self.FILE_AUTHOR = ""
        self.WARNING = ""
        self.INFO = ""

    def set_file_info(self, name: str, value: str):
        if name == 'name':
            self.FILE = value
        elif name == 'author':
            self.FILE_AUTHOR = value
        return self

    def add_command(
            self,
            command: str,
            params=None,
            usage: str = '',
            example=None):
        """
        Komanda elave eder.
        """

        self.COMMANDS[command] = {
            'command': command,
            'params': params,
            'usage': usage,
            'example': example}
        return self

    def add_warning(self, warning):
        self.WARNING = warning
        return self

    def add_info(self, info):
        self.INFO = info
        return self

    def get_result(self):
        """
        SonuÃ§ getirir.
        """

        result = f"**ð Modul:** `{self.FILE}`\n"
        if self.WARNING == '' and self.INFO == '':
            result += f"ð¥ **Official:** {'â' if self.IS_OFFICIAL else 'â'}\n\n"
        else:
            result += f"ð¥ **Official:** {'â' if self.IS_OFFICIAL else 'â'}\n"

            if self.INFO == '':
                if self.WARNING != '':
                    result += f"**â ï¸ XÉbÉrdarlÄ±q:** {self.WARNING}\n\n"
            else:
                if self.WARNING != '':
                    result += f"**â ï¸ XÉbÉrdarlÄ±q:** {self.WARNING}\n"
                result += f"**â¹ï¸ MÉlumat:** {self.INFO}\n\n"

        for command in self.COMMANDS:
            command = self.COMMANDS[command]
            if command['params'] is None:
                result += f"ð `{PATTERNS[:1]}{command['command']}`\n"
            else:
                result += f"ð `{PATTERNS[:1]}{command['command']} {command['params']}`\n"

            if command['example'] is None:
                result += f"ð  __{command['usage']}__\n\n"
            else:
                result += f"ð __{command['usage']}__\n"
                result += f"â¨ï¸ __{PATTERNS[:1]}{command['example']}__\n\n"
        return result

    def add(self):
        """
        CMD_HELP elave eder.
        """
        CMD_HELP_BOT[self.FILE] = {'info': {'official': self.IS_OFFICIAL,
                                            'warning': self.WARNING, 'info': self.INFO}, 'commands': self.COMMANDS}
        CMD_HELP[self.FILE] = self.get_result()
        return True

    def getText(self, text: str):
        if text == 'REPLY_OR_USERNAME':
            return '<isdifadeÃ§i adÄ±> <isdifadeÃ§i adÄ±/cavab>'
        if text == 'OR':
            return 'veya'
        if text == 'USERNAMES':
            return '<isdifadeÃ§i ad(lar)Ä±>'
