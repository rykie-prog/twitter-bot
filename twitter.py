# import pakgages
import pip
import tweepy
import time


# Authenticate to Twitter

consumer_key = 'eGKY0V7fB02YUzmldbcTSfIB9'
consumer_secret = 'U7RQ0nwpAca95vgwlFlvaRptEwnODKw2GnbVYNrzZhAPUol87Y'
access_key = '1063548567007215616-chPe9t9f39uI8tLO0lSmOhqdw0ZCSw'
access_secret = 'sPlvCNFjzCd2A8zx7401Ehh62pmIbEXwEsHSbtBXGpsjR'

#Create API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, parser=tweepy.parsers.JSONParser())

user = api.me()
search= 'womeninbusiness'
num_of_tweets = 1000

for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
    try:

        tweet.retweet()
        print("Retweet")
        time.sleep(0)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break        