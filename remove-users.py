# This script runs daily and checks if any users have unfollowed the bot, which would mean that they have unsubscribed.

import tweepy
import api # This opens api.py, which is not pushed to GitHub. It contains the bot's API keys.

# Initial API config
auth = tweepy.OAuthHandler(api.consumer1, api.consumer2)
auth.set_access_token(api.access1, api.access2)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

def removeUsers():
    # Get the IDs of the bot's followers
    botFollowers = api.followers_ids('NewFollowersBot')

    # Open the users file
    usersFile = open('users.txt', 'w')
    usersFileLines = usersFile.readlines

    for follower in usersFileLines:
        # For each follower that's saved
        if follower in botFollowers:
            # If they currently follow the bot
            # Do nothing
            pass
        else:
            # If they do not follow the bot (they have unfollowed)
            # Get the data from the current version (local to this program) of the file
            fileData = usersFile.read()
            # Data to remove
            data = follower + '\n'
            # Remove the data (replace it with nothing)
            fileData.replace(data, '')
            # Clear the file
            usersFile.seek(0)
            usersFile.truncate(0)
            # Write the new data
            usersFile.write(fileData)
            # Close the file
            usersFile.close()
            
            
            
            