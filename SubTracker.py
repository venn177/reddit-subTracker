import requests
import sys
import time
from datetime import datetime

SUBREDDIT_NAME = "python" # subreddit you wish to track
WAIT_TIME = 10 # minutes between logging subscriber count

currentDirectory = sys.path[0] + "\\"
headers = {
    "User-Agent": "SubTracker v0.1"
}

def get_active_users():
    url = "http://www.reddit.com/r/{}/about.json".format(SUBREDDIT_NAME)
    resp = requests.get(url, headers=headers)
    if not resp.ok:
        return -1
    content = resp.json()
    return content["data"]["accounts_active"]

def main():
    currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
    print(str(currentTime) + 'Initializing')
    try:
        currentLogFile = open(currentDirectory + 'currentLogFile.txt', 'a')
    except:
        pass
    while True:
        currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
        activeUsers = get_active_users()
        print(str(currentTime) + 'Active Users: ' + str(activeUsers))
        currentLogFile.write(str(currentTime) + str(activeUsers) + '\n')
        time.sleep(WAIT_TIME * 60)

if __name__ == "__main__":
	main()
