from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random
from constant import docs, github, sheet, api
import feijao

from greeter import Greeter

API_TOKEN = api

CONTATINHOS_SHEET_LINK = sheet
GITHUB_REPO_LINK = github
SAVED_DOCS_LINK = docs

DOCS_CHANNEL_MESSAGES_MAX = 800

greeter = Greeter()

def start(update, context):
    update.message.reply_text("pó fala meu rei")

def contatinhos(update, context):
    update.message.reply_text("CHAMA NOS CONTATINHO")
    update.message.reply_text(CONTATINHOS_SHEET_LINK, disable_web_page_preview=True)

def links(update, context):
    update.message.reply_text("""
    LINKS ÚTEIS 

    Link do grupo BCC 021: estamos adicionando todo mundo aos poucos. Se puder ajudar a achar o pessoal, tá ai: https://t.me/joinchat/ufkXtyUrI5MzZTVh

    Inscrição na semana de recepção: calouros.icmc.usp.br/

    Guia do Bixo: https://www.notion.so/Guia-do-Bixo-das-Gal-xias-EAD-Edition-1f0243e5db4b4b9a90cf6fa029a328dc#44e5291de7894f0184bc8bdfc574a4fe
    
    Contatinho de geral: https://docs.google.com/spreadsheets/d/1Kfy-tCDA_UggPUOaYs1w9oN_DtuL6GBWPyCmcl_R3f8/edit?usp=sharing

    BO FAZER BOT https://www.gabekanegae.com/creating-a-telegram-bot-with-python/""")    
    
def repo(update, context):
    update.message.reply_text(GITHUB_REPO_LINK)

def help(update, context):
    update.message.reply_text("digita \"/\" no teclado pra dar uma olhada nos comandos disponíveis :V")

def save(update, context):
    originalMessage = update.message.reply_to_message
    if not originalMessage or not originalMessage.text:
        update.message.reply_text("faz o comando respondendo alguma coisa...", parse_mode="Markdown")

    context.bot.forwardMessage("@docs21", update.effective_chat.id, originalMessage.message_id)

def docsChannel(update, context):
    update.message.reply_text(SAVED_DOCS_LINK)

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO
    )

    updater = Updater(API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("save", save))
    dp.add_handler(CommandHandler("docs", docsChannel))
    dp.add_handler(CommandHandler("contatinhos", contatinhos))
    dp.add_handler(CommandHandler("repo", repo))
    dp.add_handler(CommandHandler("feijao", feijao.sabores))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, greeter.newMembersGreetings))

    updater.start_polling()
    logging.info("=== Lineuzinho up&running! ===")
    updater.idle()
    logging.info("=== Lineuzinho shutting down :( ===")

if __name__ == "__main__":
    main()
