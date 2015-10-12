# yowbot
A bot that relays messages from Whatsapp to Telegram and vice versa.

For dealing with those pesky stubborn Whatsapp users that won't switch to Telegram.

Currently only supporting text messages, except special caracters like emoji.

##Prerequisites:
* A new Number (Buy a cheap prepaid SIM-card)
* Python3
* Pip
* [yowsup](https://github.com/tgalal/yowsup) (pip install yowsup2)
* [telegram-cli](https://github.com/vysheng/tg) (including packages listed there)
* [pytg](https://github.com/luckydonald/pytg) (pip install pytg)

##Install:
1. Install Prerequisites
2. Register Telegram number
3. Register Whatsapp number, safe number and password into run.py `CREDENTIALS`

##Launch:
1. Run tg/bin/telegram-cli -k tg/tg-server.pub -p 4458 --json
2. Run python3 yowbot/run.py

##Usage:
1. In Telegram, invite the bot to a group conversation with the whatsapp number[1] as group name. (Only the first time you message someone new in Whatsapp)
2. Start messaging in that group. Your Whatsapp buddy will receive The messages originating from a new Number, tell him to add that number as you.
3. Answers from your Whatsapp peer will appear in tht group with little delay.

[1]: Whatsapp number: Country code (eg. +41 for Switzerland) minus the plus followed by the mobile number (0781234567)  minus the first 0 resulting in 41781234567 ; adding anything else to the group name will not work.

##Features:
* [x] Messaging with individual Whatsapp users separated into Telegram Groups
* [x] Text messages
* [ ] Whatsapp Groups
* [ ] Emoji support
* [ ] Media Support
