#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from uuid import uuid4

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def help(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Digita /start per avviare il bot')
    update.message.reply_text(logger)


def start(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Ciao! Benvenuto nell helper bot di FORZA MORDOR')
    update.message.reply_text('digita /start per tornare al menu')
    update.message.reply_text('digita /potenziamento per la guida POTENZIAMENTO')
    update.message.reply_text('digita /arene per la guida alle ARENE')

def arene(bot,update):
    update.message.reply_text('digita /arene per la guida alle ARENE')
    update.message.reply_text('Preparazione all avvio: •Chi ha lenergia al massimo ha la precedenza nella creazione delle lobby necessarie al superamento dell impasse •Rispettare la fila •I pg vanno solezionati al fine di garantire le maggiori probabilità di vittoria all hoster. Quest ultimo ha sempre l ultima parola in merito •L hoster è pregato di avvisare prima di avviare l arena (es. go?; ready?; rdy?; avvio;) e aspettare la celere risposta degli altri tre membri del team (es. y; si; vai; oppure no; asp; etc) In campo: • Usare i buff solamente quando necessario o per sbloccare in tempo quello che si sa già che lo sarà presto • Il buff Spada va preso dal dps più forte in base alle specifiche del momento. Lo stesso deve, ove possibile, premurarsi di avere l abilità carica e una buona dose di hp. • Nel PvP un buff preso dal pg sbagliato è sempre meglio di un buff lasciato al nemico • Concentrare il fuoco su di un unico nemico alla volta, dando la priorità a quello che causa, direttamente o indirettamente, più danni. Non siate troppo restii dal mettere in campo i vostri orchi non appena possibile.')
    update.message.reply_text('digita /potenziamento per la guida POTENZIAMENTO')
    update.message.reply_text('digita /start per tornare al menu')

def potenziamento(bot,update):
    update.message.reply_text('Orchi e campioni andrebbero potenziati solamente quando hanno il bonus nei rispettivi power up. Fanno eccezione i pg più utili per avanzare che sono di regola un dps, un tank e un curatore. Come dps i più versatili sono Cele e Arwen (il primo single target e il secondo multi).Tra i tank il più coriaceo è Boromir, ma richiede attenzione nell uso della sua abilita altrimenti rischi di far vagabondare l avversario finendo addosso ai tuoi compagni più gracili o farlo sfuggire dalle abilità di quest ultimi.Come supporto il migliore è Hallas in quanto cura tutti gli alleati indipendentemente da dove si trovino, ha un buon attacco e velocizza l attacco degli alleati del 25% (oltre ad equivalere ad un +25% in attacco, questo significa anche caricare le abilità più velocemente). Dama è in realta quella che cura di più, tuttavia richiede che tutti gli alleati stiano fermi in un luogo per diversi secondi e questo la rende poco efficiente al di fuori delle missioni Campagna e Signori della Guerra.')
    update.message.reply_text('digita /arene per la guida alle ARENE')
    update.message.reply_text('digita /start per tornare al menu')

def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Caps",
            input_message_content=InputTextMessageContent(
                query.upper())),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                "*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                "_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN))]

    update.inline_query.answer(results)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("698253605:AAG6B_y9Eh-bMdYhIyO2gqI-nn1RwbqM7qE")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("potenziamento",potenziamento ))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("arene", arene))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
