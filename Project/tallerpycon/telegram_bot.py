import telebot # pyTelegramBotAPI
import logging # logging
import os #executing commands
from functools import wraps #to restrict users


# for executing scripts
from subprocess import call

# log settings
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/rubber_bot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# create a bot
bot = telebot.TeleBot("TELEGRAM_TOKEN")

# Restricted users
allow_username = ["@USERNAME"]

def restricted(f):
    @wraps(f)
    def wrapped(message, *args, **kwargs):
        username = message.from_user.username
        if username in allow_username:
            return f(message, *args, **kwargs)
        else:
            bot.send_message(message.chat.id, "Command forbidden for you")
    return wrapped

# help text
help_string = []
help_string.append("Welcome to rubber bot Check the options below.\n\n")
help_string.append("/start - Welcome to rubber bot\n")
help_string.append("/help - shows help menú\n")
help_string.append("/list - show the payload list\n")
help_string.append("/payload - set the payload from the list. eg: /payload NAME\n")
help_string.append("/results - show the results from the selected payload")

# --- commands

@bot.message_handler(commands=['start'])
def send_start(message):
    # send a simple message
    bot.send_message(message.chat.id, "Hi, welcome to rubber bot! Send me /help to get help.")

@bot.message_handler(commands=['help'])
def send_help(message):
    # send a message with Markdown
    bot.send_message(message.chat.id, "".join(help_string), parse_mode="Markdown")

@bot.message_handler(commands=['list'])
def send_list(message):
    try:
        # execute to list the payload list
        list = os.popen("/bin/ls tallerpycon/payloads/").read()
        bot.send_message(message.chat.id, list, parse_mode="Markdown")
    except Exception as e:
        logger.exception(str(e))
        bot.send_message(message.chat.id, "Error while getting the payloads list. Check the log for details.")

@bot.message_handler(commands=['payload'])
@restricted
def send_payload(message):
    payload = ""
    #select the argument -1 is the last element
    args = message.text.split()[-1]
    if (args == "/payload"):
        bot.send_message(message.chat.id, "Please, Select a payload from the list")
    else:
        payload = payload.join([str(elem) for elem in args])
        # execute to list the payload list
        list = os.popen("/bin/ls tallerpycon/payloads/").read()
        if (payload not in list):
             bot.send_message(message.chat.id, "Please, Select a valid payload from the list")
        else:
            try:
                os.popen('/bin/cp tallerpycon/payloads/"%s" tallerpycon/scripts/payload' %(payload))
                bot.send_message(message.chat.id, "Payload configured")
            except Exception as e:
                logger.exception(str(e))
                bot.send_message(message.chat.id, "Error while set the payload")

@bot.message_handler(commands=['results'])
@restricted
def send_results(message):
    # send the results
    data = ""
    data = open("tallerpycon/results/result","r+")
    bot.send_message(message.chat.id, data.read())
    os.popen('/bin/rm tallerpycon/results/result')


# start message receiving
bot.polling()