from telegram.ext import Updater,CommandHandler


Token = "1170278827:AAEpPtSxhDDosbKth9i1Pg9eqPI9jhrwZWY"
bot = Updater(Token)


def START (bot,update):
    
    print(update)


bot.dispatcher.add_handler(
    
    CommandHandler(

        "start",START

    )
)


bot.start_polling()
bot.idle()