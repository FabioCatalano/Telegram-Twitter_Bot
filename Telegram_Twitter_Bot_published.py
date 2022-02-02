# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:44:13 2021

@author: tarta
"""

import tweepy
import time
import requests
import os
import telebot
import random
import html

WEBSITE_URL_API='https://your_website/wp-json/wp/v2/posts'

print('\n Twitter bot')

CONSUMER_KEY = 'something' #insert here your consumer key from Twitter
CONSUMER_SECRET= 'something else'  #insert here your consumer key secret
ACCESS_KEY= 'something more' #insert here your access key
ACCESS_SECRET= 'else more' #insert here your access secret
API_TOKEN = "??????????" #insert here your bot's api token from Telegram


auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)


bot = telebot.TeleBot(API_TOKEN, parse_mode=None)
chat_id='@Chat_name' #insert here the id of the Telegram channel where you want to post your messagges

FILE_NAME='last_article_id.txt' #id of the last tweeted/posted article

#open last saved article
def retrieve_last_article(file_name):
    f_read=open(file_name,'r')
    last_article=f_read.read()
    f_read.close()
    return last_article
    

#save last article
def store_last_article(last_article,file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_article))
    f_write.close()
    return
    

#start the loop
while True:
    print("script is running...")

    last_article_id=int(retrieve_last_article(FILE_NAME))           #id of the last article on Twitter and Telegram
    r=requests.get(WEBSITE_URL_API,headers={'Cache-Control': 'no-cache'}) 
    rr=r.json()
    new_article_id=int(rr[0]['id'])   #id of the last article currently on your website
    
    
    if new_article_id!=last_article_id:
        
	#conting the number of times when the link is not correctly published
        countTW=0
        countTel=0
        
        author=rr[0]['x_author']  #store author's name
        link=rr[0]['link']        #store article's link
        title=html.unescape(rr[0]['title']['rendered'])      #store article's title 
		
                
        #send tweet
        try:
            link_preview=title+ '\n\nBy '+ author + '\n'+link     #compose message to tweet
            api.update_status(link_preview)
        except:
            try:
                time.sleep(60)
                link_preview=title+ '\n\nBy '+ author + '\n'+link  #retry if the first time fails
                api.update_status(link_preview)
            except:
                countTW=countTW+1
                print('Tweet not published',countTW, 'times')  #print if the tweet is not published


        #Send message Telegram
        try:
            text_telegram='<b>'+title+ '</b>'  + '\n\n'+ link + '\nBy ' + '<em>' + author + '</em>'  #compose Telegram message, title is in bold, author in italic
            bot.send_message(chat_id, text_telegram, parse_mode='HTML')
        except:
            try:
                time.sleep(60)
                text_telegram='<b>'+title+ '</b>'  + '\n\n'+ link + '\nBy ' + '<em>' + author + '</em>'  
                bot.send_message(chat_id, text_telegram, parse_mode='HTML')
            except:
                countTel=countTel+1
                print('Telegram message not published',countTel,'times')  
				

        store_last_article(new_article_id,FILE_NAME)  #store last article's id in the "last_article_id.txt" file
		

    time.sleep(random.randint(170,190))    #sleep around 3 minutes
    

