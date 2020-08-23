import datetime
import json

# Save data
userFollowerCountFile = open('user-follower-count.txt', 'a')
now = datetime.datetime.now()
time = str(now.strftime("%Y-%m-%d %H:%M:%S"))
screenName = 'thisisnoahevans'
followerCount = '12'

text = screenName + " --- " + followerCount + '\n'
userFollowerCountFile.write(text)
print('Saved data')
userFollowerCountFile.close()

# Read data
userFollowerCountFile = open('user-follower-count.txt', 'r')
for line in userFollowerCountFile: 
    if screenName in line:
        print("Found data")
        data = line.replace(screenName + " --- ", "")
        data = data.replace(" ", "")
        data = int(data)
        print(data)
        break
    else:
        print("No data found")
        continue