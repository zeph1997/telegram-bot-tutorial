import      #edit this line
import      #edit this line

TOKEN = ""  #edit this line with the token from botfather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"Start command was activated")


bot.polling()