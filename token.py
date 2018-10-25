import tweepy
Consumer_Key="pEgumUHODprve0bh97tc5qZeV"
Consumer_Secret="3cYpOQH6fClNI0xVq0nGg08e1nv6MQ5MBE8KqbH8B9TY9IujE2"
Access_Token="1054769431413313536-9QqE2eWarNnrPWH8obSKiirqQnfiHt"
Access_Token_Secret="Xh50qXS9fVjJvIoiFSmyMbOoyTYn2guNJKoKsgMRk9Yuo"

auth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)
api=tweepy.API(auth)
try:
	api.update_status(status="Hi all")
except  tweepy.TweepError as error:
	if error.api_code==187:
		print("Hi all")
	else:
		raise error
