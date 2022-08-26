from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram import Update
import telegram,os,json

TOKEN = os.environ["TOKEN"] #5567524975:AAHH4ioN3ZGUXbzPPPrXNk2tdWJU3O_fFyk
updater = Updater(TOKEN)
bot = telegram.Bot(TOKEN)

def echo(update:Update, context:CallbackContext):
    id = update.message.from_user.id
    text = update.message.text
    update_id = update.update_id

    #json filni ochadi va uni dict ga o'tqazadi
    with open('bot/json.json', 'r') as f:
        data = json.load(f)

    #dict jsonga malumot qo'shadi
    data[update_id] = [text,id]

    #dictni jisonga o'ytqazadi va jsonga saqlaydi
    with open('bot/json.json', 'w') as f:
        json.dump(data, f, indent=2)

    with open('bot/json.json', 'r') as f:
        data_dict = json.load(f)

    like = 0
    dithlike = 0
    for k,q in data_dict.items():
        if q[1] == id and q[0] == '👍':
            like += 1

        if q[1] == id and q[0] == '👎':
            dithlike += 1

    #like yoki dithlike ni foydalanuvchiga yuborish
    t = f"like👍:{like}\ndithlike👎:{dithlike}"
    bot.sendMessage(id, t)

    keyboer = [[telegram.KeyboardButton('👍'), telegram.KeyboardButton('👎')]]
    RKM = telegram.ReplyKeyboardMarkup(keyboer, resize_keyboard = True)
    bot.sendMessage(id, 'like', reply_markup=RKM)

updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))
updater.start_polling()
updater.idle()