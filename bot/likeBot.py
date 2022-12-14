from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram import Update
import telegram,os,json

class Like_click:
    def __init__(self):
        self.TOKEN = os.environ["TOKEN"]
        self.updater = Updater(self.TOKEN)
        self.bot = telegram.Bot(self.TOKEN)

    def likeButton(self,id):
        keyboer = [[telegram.KeyboardButton('๐'), telegram.KeyboardButton('๐')]]
        RKM = telegram.ReplyKeyboardMarkup(keyboer, resize_keyboard = True)
        self.bot.sendMessage(id, '๐๐โฅ๏ธโฅ๏ธโฅ๏ธLike Countโฅ๏ธโฅ๏ธโฅ๏ธ๐๐', reply_markup=RKM)

    def jsonDump(self,data):
        with open('bot/json.json', 'w') as f:
            json.dump(data, f, indent=2)

    def jsonLoad(self):
        with open('bot/json.json', 'r') as f:
            data = json.load(f)
        return  data

    def sendMessage(self, id, text):
        self.bot.sendMessage(id, text)

    def likeCount(self,update:Update, context:CallbackContext):
        id = update.message.from_user.id
        text = update.message.text
        update_id = update.update_id

        self.jsonDump(self.jsonLoad())
        data = self.jsonLoad()
        data[update_id] = [text,id]
        self.jsonDump(data)

        like = 0
        didnotlike = 0
        for k,q in data.items():
            if q[1] == id and q[0] == '๐':
                like += 1

            if q[1] == id and q[0] == '๐':
                didnotlike += 1

        textMessage = f"like๐-------------{like}\ndid not like๐--{didnotlike}"

        self.sendMessage(id, textMessage)
        self.likeButton(id)

like = Like_click()
like.updater.dispatcher.add_handler(MessageHandler(Filters.text,like.likeCount))
like.updater.start_polling()
like.updater.idle()