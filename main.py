import      #edit this line
from      #edit this line
import requests

TOKEN = ""  #paste the API token from BotFather inside the inverted commas

bot = telebot.TeleBot(TOKEN)
stocks = []

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"Start command was activated")

@bot.message_handler(commands=["add"])
def add_stocks(message):
    stockToAdd = message.text.strip().split()
    validityCheck = requests.get(f"", allow_redirects=False)
    if validityCheck.status_code == 200:
        stocks.append(stockToAdd[1])
        bot.send_message(message.chat.id,f"{stockToAdd[1]} added to list")
        print(stocks)
    else:
        bot.send_message(message.chat.id,"Wrong code entered. Please try again")

@bot.message_handler(commands=["getprice"])
def get_price(message):
    output_message = ""
    stocks = []
    bot.send_message(message.chat.id,"Getting prices...")
    for stock in stocks:
        url = f""
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        price = soup.select("")[0].text.strip()
        timing = soup.select("")[0].text.strip()
        message += f"Price of {i} \n${price}, {timing} \n"
    bot.send_message(message.chat.id,output_message)

bot.polling()