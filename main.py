import      #edit this line
from      #edit this line
import requests

TOKEN = ""  #paste the API token from BotFather inside the inverted commas

bot = telebot.TeleBot(TOKEN)
stocks = []

@bot.message_handler(commands=["start"])
def start_message(message):
    #add a reply to the user here

@bot.message_handler(commands=["add"])
def add_stocks(message):
    stockToAdd = message.text.strip().split()
    #the line below checks the website to see if the stock exists. If it exists, then we will add it into a list for them. If not, we will tell the user that the code is invalid. 
    validityCheck = requests.get(f"", allow_redirects=False)    #add website URL here
    if validityCheck.status_code == 200:
        stocks.append(stockToAdd[1])
        bot.send_message(message.chat.id,f"{stockToAdd[1]} added to list")
        print(stocks)
    else:
        bot.send_message(message.chat.id,"Wrong code entered. Please try again")

@bot.message_handler(commands=["getprice"])
def get_price(message):
    output_message = ""
    bot.send_message(message.chat.id,"Getting prices...")
    for stock in stocks:
        url = f""       #add website URL here
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        price = soup.select("")[0].text.strip()     #add the element that contains the stock price here
        timing = soup.select("")[0].text.strip()    #add the element that contains the time here
        output_message += f"Price of {stock} \n${price}, {timing} \n"
    bot.send_message(message.chat.id,output_message)

bot.polling()
