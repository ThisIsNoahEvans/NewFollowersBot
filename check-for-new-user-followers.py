# This is the main script, where all of the bot /\magic\/ happens.

import tweepy
import api # This opens api.py, which is not pushed to GitHub. It contains the bot's API keys.

# Initial API config
auth = tweepy.OAuthHandler(api.consumer1, api.consumer2)
auth.set_access_token(api.access1, api.access2)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

def checkForNewUserFollowers():
    # Open the users file in read mode
    usersFile = open('users.txt', 'r')
    # Get the lines
    users = usersFile.readlines
    for user in users:
        # For each user in the users file (one per line, their account ID)
        user = str(user)
        # Remove the blank line
        user = user.replace('\n', '')
        # Open the user's file (named their ID)
        userFile = open(user, 'w+')
        # Get the lines
        usersFollowers = userFile.readlines
        
        # Get their current followers
        usersFollowers = api.followers_ids(user)
        # Get their current follower count
        currentFollowerCount = int(len(usersFollowers))

        # Open the follower count file in write mode
        userFollowerCountFile = open('user-follower-count.txt', 'w')
        userFollowerCountFileLines = userFollowerCountFile.readlines
        for line in userFollowerCountFileLines:
            # For each line in the file
            if user in line:
                # If the user's ID is in the file (it should be...)
                # Remove the unneeded info
                oldFollowerCount = line.replace(user + " --- ", "")
                oldFollowerCount = oldFollowerCount.replace(" ", "")
                # Convert to an integer
                oldFollowerCount = int(oldFollowerCount)

                if currentFollowerCount > oldFollowerCount:
                    # User gained followers
                    # Find the difference (new followers) | current - old = difference
                    newFollowers = currentFollowerCount - oldFollowerCount

                    if newFollowers > 10:
                        # User gained more than 10 followers, will not send exact usernames
                        # Get the user's screen name
                        userData = api.get_user(user)
                        screenName = userData.screen_name
                        # Compose message
                        message = f'👋 @{screenName}, it\'s that time again! Since we last spoke, you\'ve gained {newFollowers} new followers. Have a great week!'
                    else:
                        # User gained lest than 10 followers, will send exact usernames
                        # Get the user's screen name
                        userData = api.get_user(user)
                        screenName = userData.screen_name
                        # Compose message
                        message = f'👋 @{screenName}, it\'s that time again! Since we last spoke, you\'ve gained {newFollowers} new followers. These are... Have a great week!'

                if currentFollowerCount < oldFollowerCount:
                    # User lost followers
                    # Find the difference (new followers) | old - current = difference
                    newFollowers = oldFollowerCount - currentFollowerCount

                    if newFollowers > 10:
                        # User gained more than 10 followers, will not send exact usernames
                    else:
                        # User gained lest than 10 followers, will send exact usernames

                if currentFollowerCount == oldFollowerCount:
                    # User gained/lost no followers
                    


            else:
                # If something somehow went wrong
                print("No data found")
                continue