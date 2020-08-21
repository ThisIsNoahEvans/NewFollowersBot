# Plan
## This is my initial plan I wrote before coding the bot, and (should) correspond to comments in the Python files.

### Check For New Bot Followers
#### Details
* Run every day at 12am (crontab)
* Saves new users to file
#### Actions
* Get the IDs of the bot’s followers
* For each ID (person who follows the bot):
    * Get their username
    * Open the users file
        * Check if the username is already saved
            * If so, move to the next ID
        * If the username is not saved
            * Save the username to the users file
            * Get the IDs of their followers
            * Save the user’s followers to a file named their ID

### Check For New User Followers
#### Details
* Compare the current followers of each subscriber with the data in their file
* Message them with the difference
    * e.g. “You have gained 6 followers in the last week. These are @….”, “You have lost 2 followers in the last week. These are @….”
- Update their file with their current followers
#### Actions
* For each username in the username file:
    * Get the IDs of their followers
    * Open their file
        * Compare the two: e.g. 3 IDs have been added
            * For each new ID / removed ID, get their username
        * Compose and send the message - e.g. “You have gained 6 followers in the last week. These are @….”, “You have lost 2 followers in the last week. These are @….”
    * Update the user’s file with their current IDs
