import tweepy
import api


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
        # Get the user's screen name
        userData = api.get_user(userID)
        userScreenName = userData.screen_name
        # Open the users file in read mode
        with open('users.txt') as usersFileRead:
            # Check if the user's screen name is already saved
            if userScreenName in usersFileRead:
                print('User', userScreenName, 'is already saved')
                usersFileRead.close()
            # If the user's screen name is not already saved
            else:
                usersFileRead.close()
                # Open the users file in edit mode
                usersFileWrite = open('users.txt', 'a')
                # Save the user's screen name
                usersFileWrite.append(userScreenName, '\n')
                print('Saved user', userScreenName, 'to users file')
                # Create and open the user's file
                usersFileName = userID + '.txt'
                userFile = open(usersFileName, "a+")
                # Get the user's followers
                usersFollowers = api.followers_ids(userScreenName)
                for usersFollower in usersFollowers:
                    userFollowerCount = userFollowerCount + 1
                    writeData = str(usersFollower)
                    userFile.write(writeData + '\n')
                    print('Saved follower', usersFollower, 'to file for', userScreenName, 'with ID (filename) of', userID)
                print('Saved all followers of', userScreenName, 'to file for', userScreenName, 'with ID (filename) of', userID)


checkForNewBotFollowers()