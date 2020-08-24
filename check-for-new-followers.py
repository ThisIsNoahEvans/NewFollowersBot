# This script adds new accounts who have followed @NewFollowersBot to the system, and saves their current follower data.

import tweepy
import api # This opens api.py, which is not pushed to GitHub. It contains the bot's API keys.

# Initial API config
auth = tweepy.OAuthHandler(api.consumer1, api.consumer2)
auth.set_access_token(api.access1, api.access2)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

botFollowers = []
botUsername = 'NewFollowersBot'

userFollowerCount = 0

def checkForNewBotFollowers():
    # Get the IDs of the bot's followers
    for page in tweepy.Cursor(api.followers_ids, screen_name=botUsername).pages():
        botFollowers.extend(page)

    # For each ID (user who follows the bot)
    for userID in botFollowers:
        # Get the user's data and screen name
        userData = api.get_user(userID)
        userScreenName = userData.screen_name
        # Open the users file in read mode
        usersFileRead = open('users.txt', 'r')
        # Check if the user's screen name is already saved
        if userID in usersFileRead:
            print('User', userScreenName, 'is already saved')
            usersFileRead.close()
            continue
        # If the user's screen name is not already saved
        else:
            usersFileRead.close()
            # Open the users file in edit mode
            usersFileWrite = open('users.txt', 'a')
            # Save the user's ID (we use account IDs for simplicity reasons)
            usersFileWrite.append(userID, '\n')
            print('Saved user', userScreenName, 'to users file')
            # Create and open the user's file
            usersFileName = userID + '.txt'
            userFile = open(usersFileName, "a+")
            # Get the IDs of the user's followers
            usersFollowers = api.followers_ids(userScreenName)
            # For each follower
            for usersFollower in usersFollowers:
                userFollowerCount = userFollowerCount + 1
                writeData = str(usersFollower)
                # Save each follower to their file
                userFile.write(writeData + '\n')
                print('Saved follower', usersFollower, 'to file for', userScreenName, 'with ID (filename) of', userID)
            print('Saved all followers of', userScreenName, 'to file for', userScreenName, 'with ID (filename) of', userID)
            # Close the file
            userFile.close()

            # Open the follower count file
            userFollowerCountFile = open('user-follower-count.txt', 'a')
            # Compose the data to be saved
            data = userID + " --- " + userFollowerCount + '\n' # This is an INCREDIBLY dodgy way of doing things, so do as I say, not as I do kids
            # Write the data
            userFollowerCountFile.append(data)
            print('Saved the user', userScreenName, 'and their follower count of', userFollowerCount, 'to the file')
            # Close the file
            userFollowerCountFile.close()


# checkForNewBotFollowers()