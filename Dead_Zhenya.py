#!/usr/bin/env python3
 # -*- coding: utf-8 -*-
'''
The Degenerate Bot, Zhenya. Parse the token into the start_zhenya function or with -q if launching as script.
'''
import markovify
import pandas as pd
import logging
import argparse
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Create bot entity with API

def start(bot, update):
    '''
    Define the /start command
    '''
    bot.send_message(chat_id=update.message.chat_id, text="""
Добро пожаловать к самому дегенеративному боту.
/olo чтобы сгенерировать рандомную дегенеративность.
/with _word_, чтобы сгенерировать дегенеративность начинающуюся c _word_""")

def olo(bot, update):
    '''
    Generate random message (/start command)
    '''
    bot.send_message(chat_id=update.message.chat_id,
                     text=text_model.make_short_sentence(140).lower())

def OLO(bot, update):
    '''
    Generate random message (/start command)
    '''
    bot.send_message(chat_id=update.message.chat_id,
                     text=text_model.make_short_sentence(140).upper())

def error(bot, update, error):
    '''
    Print warnings in case of errors
    '''
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"',
                   update,
                   error)

def OLO_start(bot, update, args):
    '''
    Generate random message starting from words given (/with command)
    '''
    argument = ' '.join(args)
    try:
        reply = text_model.make_sentence_with_start(argument.lower(), strict=False)
    except:
        bot.send_message(chat_id=update.message.chat_id,
                     text='Недостаточно дегенеративности(((99((9')
        return
    if reply is None:
        bot.send_message(chat_id=update.message.chat_id,
                     text='Недостаточно дегенеративности(((99((9')
    else:
        bot.send_message(chat_id=update.message.chat_id,
                     text=reply)

def ORY(bot, update):
    '''
    Reply to the shouting
    '''
    mes = update.message.text
    if 'ору' in mes.lower():
        update.message.reply_text("Не ори")



def start_zhenya(token):
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    # Read the data

    # Config the logger
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Create the text model
    # Add all the handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('olo', olo))
    dispatcher.add_handler(CommandHandler('oloo', OLO))
    dispatcher.add_handler(MessageHandler(Filters.text, ORY))
    dispatcher.add_handler(CommandHandler('with', OLO_start, pass_args=True))
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    # idle is better than just polling, because of Ctrl+c
    updater.idle()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-t", help="your bot API token", type=str)
    args = parser.parse_args()
    print(args.t)
    df = pd.read_csv('./OLO.tsv', sep='\t', index_col=0)
    text_model = markovify.NewlineText(df.Clean.astype(str).str.lower(), state_size=2)
    start_zhenya(token=args.t)
