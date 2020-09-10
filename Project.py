from telegram.ext import Updater,CommandHandler


Token = "1170278827:AAEpPtSxhDDosbKth9i1Pg9eqPI9jhrwZWY"
bot = Updater(Token)


def START (bot,update):

    message = update.message
    chat = message.chat
    message_id = message.message_id
    chat_id = chat.id
    first_name = chat.first_name
    text = message.text

    if "username" in chat:
        username = chat.username

    print(message,chat,message_id,chat_id,first_name,text,username)

    


bot.dispatcher.add_handler(
    
    CommandHandler(

        "start",START

    )
)


bot.start_polling()
bot.idle()