# This is the main script, where all of the bot /\magic\/ happens.

import tweepy
import api # This opens api.py, which is not pushed to GitHub. It contains the bot's API keys.

# Initial API config
auth = tweepy.OAuthHandler(api.consumer1, api.consumer2)
auth.set_access_token(api.access1, api.access2)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

newFollowersArray = []


def checkForNewUserFollowers():
    userFollowerCount = 0

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
                # This is for later
                originalFollowerCountFileUser = line
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
                        message = f'👋 @{screenName}, it\'s that time again! Since we last spoke, you\'ve gained {newFollowers} new followers. 😄 Have a great week!'
                        # Send message
                        api.send_direct_message(user, message)
                    if newFollowers <= 10:
                        # User gained less than 10 followers, will send exact usernames
                        # Get the user's screen name
                        userData = api.get_user(user)
                        screenName = userData.screen_name
                       
                        # Beginning of message
                        message = f'👋 @{screenName}, it\'s that time again! Since we last spoke, you\'ve gained {newFollowers} new followers. 😄 These are '
                      
                        # Get followers that are new
                        for follower in usersFollowers:
                            # For each follower in the current followers array
                            if follower not in usersFile:
                                # If the new follower is not in the user's file (they are new)
                                # Get the follower's screen name
                                newFollowerScreenName = api.screen_name(follower)
                                newFollowerScreenName = '@' + newFollowerScreenName + ', '
                                # Update message to its current content plus the new follower's screen namee
                                message = message + newFollowerScreenName

                        # Remove the extra space / comma
                        message = message[:-2]
                        # Add the ending part
                        message = message + '. Have a great week!'
                        # Send message
                        api.send_direct_message(user, message)
                             

                if currentFollowerCount < oldFollowerCount:
                    # User lost followers
                    # Find the difference (new followers) | old - current = difference
                    lostFollowers = oldFollowerCount - currentFollowerCount

                    if lostFollowers > 10:
                        # User lost more than 10 followers, will not send exact usernames
                        # Get the user's screen name
                        userData = api.get_user(user)
                        screenName = userData.screen_name
                        # Compose message
                        message = f'👋 @{screenName}, it\'s that time again! Since we last spoke, you\'ve lost {newFollowers} followers. 😔 Have a great week!'
                        # Send message
                        api.send_direct_message(user, message)

                    if newFollowers <= 10:
                        # User lost less than 10 followers, will send exact usernames
                        # Get the user's screen name
                        userData = api.get_user(user)
                        screenName = userData.screen_name
                       
                        # Beginning of message
                        message = f'👋 @{screenName}, it\'s that time again! Since we last spoke, you\'ve lost {newFollowers} followers. 😔 These are '
                      
                        # Get followers that have unfollowed
                        for follower in userFile:
                            # For each follower in the the user's own file
                            if follower not in usersFollowers:
                                # If the follower is not currently following (they have unfollowed since last check)
                                # Get the follower's screen name
                                oldFollowerScreenName = api.screen_name(follower)
                                oldFollowerScreenName = '@' + oldFollowerScreenName + ', '
                                # Update message to its current content plus the new follower's screen namee
                                message = message + oldFollowerScreenName
                                

                        # Remove the extra space / comma
                        message = message[:-2]
                        # Add the ending part
                        message = message + '. Have a great week!'
                        # Send message
                        api.send_direct_message(user, message)

                if currentFollowerCount == oldFollowerCount:
                    # User gained/lost no followers
                    # Get the user's screen name
                    userData = api.get_user(user)
                    screenName = userData.screen_name
                    # Compose the message
                    message = f'👋 @{screenName}, it\'s that time again! Since we last spoke, you haven\'t lost or gained any new followers. 🙈 Have a great week!'
                    # Send message
                    api.send_direct_message(user, message)

            else:
                # If something somehow went wrong
                print("No data found")
                continue
    
    # Update the user's file
    # Empty the file - truncate it to 0 chars
    usersFile.truncate(0)
    
    for usersFollower in usersFollowers:
        # For each current follower
        # Add to the count
        userFollowerCount = userFollowerCount + 1
        writeData = str(usersFollowers)
        # Save each follower to the user's file
        usersFile.write(writeData + '\n')

    
    # Update the follower count file
    # Compose the data to be saved
    data = user + '---' + currentFollowerCount + '\n' # This is an INCREDIBLY dodgy way of doing things, so do as I say, not as I do kids
    # Get the data from the current version of the file
    fileData = userFollowerCountFile.read()
    # Replace the data
    fileData = fileData.replace(originalFollowerCountFileUser, data)
    # Clear the file
    userFollowerCountFile.seek(0)
    userFollowerCountFile.truncate(0)
    # Write the new data
    userFollowerCountFile.write(fileData)
    # Close the file
    userFollowerCountFile.close()


# Uncomment before deploying this program 
# checkForNewUserFollowers()