# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info."
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to {PROJECT_NAME}


🦊 Contributors
- @XFLSkyzo

Want to add me to your group?Add me to your group!

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Setting up**

**1) Make bot admin (Group and in channel if use cplay)**
**2) Start a voice chat**
**3) Try /play [song name] for the first time by an admin**
**4) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry**

**For Channel Music Play**
**1) Make me admin of your channel**
**2) Send /userbotjoinchannel in linked group**
**3) Now send commands in linked group**
""",
f"""
**Commands**

**➠ Song Playing**

**- /play: Play the requestd song**
**- /play [yt url] : Play the given yt url**
**- /play [reply yo audio]: Play replied audio**
**- /dplay: Play song via deezer**
**- /splay: Play song via jio saavn**
**- /ytplay: Directly play song via Youtube Music**

**➠ Playback**

**- /player: Open Settings menu of player**
**- /skip: Skips the current track**
**- /pause: Pause track**
**- /resume: Resumes the paused track**
**- /end: Stops media playback**
**- /current: Shows the current Playing track**
**- /playlist: Shows playlist**

**Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.**
""",

f"""
**➠ Channel Music Play**

⚪️ **For linked group admins only:**

**- /cplay [song name] - play song you requested**
**- /cdplay [song name] - play song you requested via deezer**
**- /csplay [song name] - play song you requested via jio saavn**
**- /cplaylist - Show now playing list**
**- /cccurrent - Show now playing**
**- /cplayer - open music player settings panel**
**- /cpause - pause song play**
**- /cresume - resume song play**
**- /cskip - play next song**
**- /cend - stop music play**
**- /userbotjoinchannel - invite assistant to your chat**

**( /cplay = /channelplay )**

**⚪️ If you donlt like to play in linked group:**

**1) Get your channel ID.**
**2) Create a group with tittle: Channel Music: your_channel_id**
**3) Add bot as Channel admin with full perms**
**4) Add @{ASSISTANT_NAME} to the channel as an admin.**
**5) Simply send commands in your group. (use /ytplay instead /play)**
""",

f"""
**➠ More Tools**

**- /musicplayer [on/off]**
**- /admincache**
**- /userbotjoin**
""",
f"""
**➠ Song Download**

**- /video [song mame]**
**- /song [song name]**
**- /saavn [song name]**
**- /deezer [song name]**

**➠ Search Tools**

**- /search [song name]**
**- /lyrics [song name]**
""",

f"""
**➠ Commands for Sudo Users**

 **- /userbotleaveall**
 **- /broadcast <reply to message>**
 **- /pmpermit [on/off]**
**Sudo Users can execute any command in any groups**

"""
      ]
