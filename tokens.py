import tweepy 
consumer_key="Fgh9Lcslz63lvG2ovJawOnyqH"
consumer_secret_key="ePLQgfjsDT7QDtl32bqvGtBkJeQieXAV2TfAe8wl4pKffPAImA"
access_token="1054451670506078208-ZuVU9oZabrAmY9I7DzMQnWitgYyoMF"
access_token_secret="RFNLjt491rwxcjETjXH8Vn1XLdXDmgX7MpAi9O5vw1BM8"
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
