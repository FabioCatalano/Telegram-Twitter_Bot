# Telegram-Twitter_Bot
Create a bot that publishes on Twitter and Telegram the articles posted on your website

The code uses the following modules: tweepy, time, requests, os, telebot, random and html. You have to get your Twitter's keys from Twitter Developer portal (https://developer.twitter.com/en/docs/developer-portal/overview) and create a Telegram bot with "BotFather" (https://t.me/botfather). 

The posted code saves the id of the last published articles in a separate file called "last_article_id.txt" and then it checks every 3 minutes if a new one has been published on the website. 
