# telegram-bot-tutorial

<b>What you will learn:</b>
<ol>
  <li>A brief intro to the basic building blocks of Websites (HTML, CSS)</li>
  <li>How to import packages to your project</li>
  <li>How to connect to Telegram</li>
  <li>How to webscrape</li>
  <li>How to respond to user input</li>
</ol>
<br>
<b>What you will need to have:</b>
<ol>
  <li>Python installed (minimum python 3). Please click <a href="https://www.python.org/downloads/">here</a> if you have not done so</li>
  <li>An IDE. Any IDE is fine, but preferably VS Code so it will be easier to follow. Please click <a href="https://code.visualstudio.com/">here</a> if you wish to download VS Code.</li>
</ol>
<br>
<h2>1. A brief intro to the basic building blocks of Websites</h2>
HTML stands for Hyper Text Markup Language and CSS stands for Cascading Style Sheet. These are the building blocks of all websites around the world.<br>
<br>
<img src="/README/inspect.png"><br>
Right click on any website page and click on "Inspect". You will see a window on the side of the page. That is content of the page. The computer takes that chunk of text and converts it into the nice pages you see today. HTML produces the content, while CSS helps style the website to make it look nice and colourful.<br>
<br>
In this workshop we will not be writing any HTML or CSS, but it is necessary for us to understand how the website looks like under the hood to be able to webscrape.
<br>
<h2>2. How to import packages to your project</h2>
Download this repository and open up the <code>main.py</code> file using VS Code or any IDE of your preference.<br>
You will see <code>import</code> on the first two lines. We will have to utilise some packages (which are code other people wrote) to help us connect to Telegram. In order to get the package to connect to Telegram, we need to use the command prompt.<br>
<br>
<b>Follow these steps to install pyTelegramBotAPI and BeautifulSoup:</b><br>
&emsp;<b>Step 1:</b> Go to the search bar and type <code>cmd</code> <br>
&emsp;<b>Step 2:</b> Click on command prompt <br>
&emsp;<b>Step 3:</b> Type in <code>pip install pyTelegramBotAPI</code>. (This is an API written by <a href="https://github.com/eternnoir/pyTelegramBotAPI">eternnoir</a> that allows us to connect to Telegram using python)<br>
&emsp;<b>Step 4:</b> Go to <code>main.py</code> on your IDE and fill in line 1 with <code>import telebot</code><br>
&emsp;<b>Step 5:</b> Go back to the command prompt and type <code>pip install beautifulsoup4</code> (This is an API to help us extract out the contents from websites)<br>
&emsp;<b>Step 6:</b> Go back to <code>main.py</code> on your IDE and fill in line 2 with <code>from bs4 import BeautifulSoup</code> (This helps us import only the necessary functions needed for our process) <br>
<br>
Now you have all the tools to start building your own webscraping bot!
<br>
<h2>3. How to connect to Telegram</h2>
Time for us to create a bot! Go into Telegram and search for <code>BotFather</code><br>
<br>
Tap "START" and type <code>/newbot</code> to create your own bot. Follow the instructions to give your bot any name you like. Once you've given the bot a name and username, BotFather will give you an API Token. <br>
<img src="/README/apikey.png"><br>
<b>Please do not share this token as anyone with it will be able to control your bot!<b><br>
<br>
Copy the API Token and go back to <code>main.py</code>. Paste the API Token in line 5, inside the inverted commas. Make sure that the API Token has the inverted commas before and after it.<br>
<br>
Now your bot is connected to Telegram!<br>
<h2>4. How to Webscrape</h2>
As mentioned in the first section, the content on the websites are mostly in HTML. As such, we can find the target elements and extract the specific information. Lucky for us, we have BeautifulSoup to help us with that. BeautifulSoup can isolate elements in the page will make it easier for us to extract a certain piece of information on the website (e.g. the text of the price of an item on the website.<br>
<h2>5. How to respond to user input on Telegram</h2>
To reply to a message, we have to include a message handler. You can see these on line 10, 14, and 25. They will handle the responses of the specified user input. Let us use line 10 as an example. You can see that <code>commands=["start"]</code> is within the brackets of the message handler. This means that the following code underneath the message handler will be executed when the user types <code>/start</code><br>
<br>
As mentioned above, the message handlers are always followed with a function (e.g. line 11). They usually start with the word <code>def</code> followed by the name of the function and a variable as a parameter. The name of the function can be any name decided by you. The parameter refers to the message sent by the user. You can extract useful information such as the chat ID of the user (to be used to reply to them) or even the whole text of the message. Take note that any command messages have to be preceeded with a <code>/</code><br>
<br>
To reply to a specific user, use the <code>.send_message</code> function (as seen on line 12). The required arugement is the user chat id, which can be retrieved from the parameter as mentioned in the paragraph above. Use <code>message.chat.id</code> to get the chat ID. For those who are interested, the message information retrieved as a parameter for the function is a dictionary, which allows it to store mutliple data as long as we know how to access them. You can always <code>print()</code> the variable to be able to see the contents in greater detail (which will be useful for debuggin).<br>
<br>
After putting the chat ID of the user to reply, add a comma <code>,</code> and start typing the message that you would like to send to the user. Do remember that the message will have to be a string data type so you have to enclose your text in inverted commas.<br>
<br>
Now add <code>bot.polling</code> way below your code (as seen on line 39) to get the bot to listen on Telegram. <b>Make sure it is at the end of all the code as the bot will not read the code after the polling function is called.</b><br>
<br>
<h2>Well Done!</h2>
Andddd..... you're all set! Now just right click on the IDE and click <code>Run Python File in Terminal</code> and you can start using your bot! Do note that the file has to be running in the terminal in order for the bot to be live. To shut down the bot, you can use CTRL+C in the terminal. Congratulations on creating your first bot! 
