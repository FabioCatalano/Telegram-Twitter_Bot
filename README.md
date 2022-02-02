# Telegram-Twitter_Bot
Create a bot that publishes on Twitter and Telegram the link to the articles you have posted on your website

The code uses the following modules: <b>tweepy</b>, <b>time</b>, <b>requests</b>, <b>os</b>, <b>telebot</b>, <b>random</b> and <b>html</b>. You have to get your Twitter's keys from the Twitter Developer portal (https://developer.twitter.com/en/docs/developer-portal/overview) and create a Telegram bot with "BotFather" (https://t.me/botfather). 

The posted code saves the id of the last published article in a separate file called "last_article_id.txt" and then it checks if a new one has been published on the website through the 2 functions "retrieve_last_article" and "store_last_article".

In the infinite loop the id of the last article currently published on Twitter and Telegram is read. Then the id of the last article currently on the website is checked through the module "requests" and this is stored in the variable "new_article_id". 

If the 2 ids are different the link of the new article together with some other information like author and title is published in the chosen Telegram channel and on the Twitter profile. The program tries to send the message or publish the tweet 2 times. If both fail an error message is returned, but the program doesn't stop. 

