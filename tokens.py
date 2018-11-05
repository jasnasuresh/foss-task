import tweepy 
consumer_key=" "
consumer_secret_key=" "
access_token=" "
access_token_secret=" "
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token, access_token_secret) 
api=tweepy.API(auth) 
try:
    api.update_status("This is my first tweet!")
except tweepy.TweepError as error:
    if error.api_code == 187:
        print("This is my first tweet!")
    else:
       	raise error
