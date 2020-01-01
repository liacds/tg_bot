import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import telebot
cred = credentials.Certificate('cred.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
f = open("tgapi.txt", "r+")
token =f.read()
f.close()
bot = telebot.TeleBot(token)

class firebase():

    def sendMessage(self, company, prefix, links, title, location):
        for link in links:
            docs = db.collection(u''+company+'Links').where(u'link', u'==', link).stream()
            if (sum(1 for doc in docs) == 0):
                db.collection(u''+company+'Links').add({'link': link})
                index = links.index(link)
                thistitle = title[index]
                thislocation = location[index]
                users = db.collection(u''+company+'').stream()
                for user in users:
                    bot.send_message(user.id, self.beautifulText(prefix, link, thistitle, thislocation))

    def beautifulText(self, prefix, link, title, location):
            link2 = prefix + link + " "
            title2 = title + " "
            location2 = "Location: " +location+" "
            return title2 + link2+location2