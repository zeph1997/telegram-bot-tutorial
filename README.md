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
<b>Follow these steps to install pyTelegramBotAPI and BeautifulSoup:</b><br>
<b>Step 1:</b> Go to the search bar and type <code>cmd</code> <br>
<b>Step 2:</b> Click on command prompt <br>
<b>Step 3:</b> Type in <code>pip install pyTelegramBotAPI</code>. (This is an API written by eternnoir that allows us to connect to Telegram using python)<br>
<b>Step 4:</b> Go to <code>main.py</code> on your IDE and fill in line 1 with <code>import telebot</code><br>
<b>Step 5:</b> Go back to the command prompt and type <code>pip install beautifulsoup4</code> (This is an API to help us extract out the contents from websites)<br>
<b>Step 6:</b> Go back to <code>main.py</code> on your IDE and fill in line 2 with <code>from bs4 import BeautifulSoup</code> (This helps us import only the necessary functions needed for our process) <br>
<br>
Now you have all the tools to start building your own webscraping bot!
<br>
<h2>How to connect to Telegram</h2>
