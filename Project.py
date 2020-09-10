from telegram.ext import Updater,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup


Token = "1170278827:AAEpPtSxhDDosbKth9i1Pg9eqPI9jhrwZWY"
bot = Updater(Token)


def START (bot,update):

    message = update.message
    chat = message.chat
    message_id = message.message_id
    chat_id = chat.id
    first_name = chat.first_name
    text = message.text


    if "username" in "{}".format(update.message.chat):
        username = chat.username    

    else:
        username = None


    KEYBOARD_START_1 = [

       [InlineKeyboardButton('راهنما',callback_data= "sabtenam")]

    ]
    REPLY_MARKUP = InlineKeyboardMarkup(KEYBOARD_START_1)


    bot.send_message (

        chat_id = chat_id , text = "_خوش آمدید_\n\n برای شروع ابتدا برروی راهنما کلیک کنید.\n\n📢❗️📢❗️📢", parse_mode='markdown', reply_markup = REPLY_MARKUP

    )

def CALLBACK_DATA (bot,update):
    
    bot.answer_callback_query(update.callback_query.id,"لطفا شماره همراه خود را وارد کنید")

    
def MESSAGE (bot,update):

    pass



bot.dispatcher.add_handler(
    
    CommandHandler(

        "start",START

    )
)


bot.dispatcher.add_handler(

    CallbackQueryHandler(

        CALLBACK_DATA
    )
)


bot.start_polling()
bot.idle()