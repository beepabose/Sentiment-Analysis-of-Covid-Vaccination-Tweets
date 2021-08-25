import tweepy
import pandas as pd
import numpy as np
from datetime import datetime,timedelta


consumer_key = "SgEEAKQlKAe2aKLj4LX6ehIaY"
consumer_secret = "LmFrHmxIh9bibBFE22e9CvNaf6Rbl2lzZguRGPJSMBRpLGCKdU"
access_token = "481284830-Gc21i7lRvpULdMILilqgmN79RJ7zKTDOoNZS2xQ6"
access_token_secret = "3dFitz3StxiyBpPJb1iZOcylSsvhJlJIliJuBluJ2V9rg"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
search_words = ["#vaccine","#covid19"]

date = ["2021-04-27","2021-04-28","2021-04-29","2021-04-30","2021-05-01","2021-05-02"]
for date in date:
    filename="Raw-CovidTweet"+str(date)+".csv"
    print(filename)
    date_since = date
    f=datetime.strptime(date, '%Y-%m-%d')+timedelta(days=1)
    date_until = str(f.year)+'-'+str(f.month)+'-'+str(f.day)
    i=0
    tweets = tweepy.Cursor(api.search, q=search_words, lang="en",since=date_since,until=date_until).items(2000)
    data1 = pd.DataFrame()
    for tweet in tweets:
        i=i+1
        name = tweet.user.screen_name
        text = tweet.text
        retweets = tweet.retweet_count
        location = tweet.user.location
        created = tweet.created_at.strftime("%d-%b-%Y")
        followers = tweet.user.followers_count
        is_user_verified = tweet.user.verified
        S1= pd.Series([name,text, retweets,location,created,followers,is_user_verified],index=['name','text','retweets','location','created','followers','is_user_verified'])
        data1=data1.append(S1,ignore_index=True)
    data1.to_csv(filename)
    

