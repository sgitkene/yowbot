# yowbot
A bot that relays messages from Whatsapp to Telegram and vice versa.

Currently only supporting text messages, except special caracters like emoji.

##Prerequisites:
Python3
Pip
https://github.com/tgalal/yowsup (pip install yowsup)
https://github.com/vysheng/tg
https://github.com/luckydonald/pytg (pip install pytg)

##install:
1. Install Prerequisites
2. Register Telegram number
3. Register Whatsapp number, safe number and password into run.py CREDENTIALS

##launch:
1. Run tg/bin/telegram-cli -k ../tg-server.pub -p 4458 --json
2. Run python3 yowbot/run.py
3. (only once with every whatsapp peer you want to talk to) From your own tg account invite the bot to a conversation with the number of the whatsapp peer you want to chat with. start messaging in that group.

