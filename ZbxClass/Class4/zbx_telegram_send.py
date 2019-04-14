import telebot
import sys

BOT_TOKEN=sys.argv[1]
DEST = sys.argv[2]
SUBJECT = sys.argv[3]
MSG = sys.argv[4]

MSG = MSG.replace('/n','\n')

tb = telebot.TeleBot(BOT_TOKEN)
tb.send_message(DEST,SUBJECT + '\n' + MSG) 
