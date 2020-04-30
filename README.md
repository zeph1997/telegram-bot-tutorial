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
Right click on any website page and click on "Inspect". You will see a window on the side of the page. That is content of the page. The computer takes that chunk of text and converts it into the nice pages you see today. HTML produces the content, while CSS helps style the website to make it look nice and colourful. In this workshop we will not be writing any HTML or CSS, but it is necessary for us to understand how the website looks like under the hood to be able to webscrape.
<br>
<h2>2. How to import packages to your project</h2>
Download this repository and open up the <code>main.py</code> file using VS Code or any IDE of your preference.<br>
You will see <code>import</code> on the first two lines. We will have to utilise some packages (which are code other people wrote) to help us connect to Telegram. In order to get the package to connect to Telegram, we need to use the command prompt.<br>
Go to the search bar and type <code>cmd</code>. Click on command prompt and type <code>pip install pyTelegramBotAPI</code>. This is an API written by eternnoir that allows us to connect to Telegram using python.<br>
Now go back to <code>main.py</code> line 1 and fill in the first line with <code>import telebot</code>
