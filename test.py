# This file is for quick tests I may need to make during development.


import tweepy
import api


# Initial API config
auth = tweepy.OAuthHandler(api.consumer1, api.consumer2)
auth.set_access_token(api.access1, api.access2)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)




subscriberFollowers = api.followers_ids('whatcookingapp')
subscriberFile = open('testfile.txt', "a+")
for subscriberFollower in subscriberFollowers:
    writeData = str(subscriberFollower)
    subscriberFile.write(writeData + '\n')