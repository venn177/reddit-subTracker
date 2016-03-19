import praw
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
    print(str(currentTime) + 'Logging in...')
    r = praw.Reddit(user_agent = 'SubTracker v0.1')
    subToWatch = r.get_subreddit(SUBREDDIT_NAME)
    try:
        subLogFile = open(currentDirectory + 'subLogFile.txt', 'a')
        currentLogFile = open(currentDirectory + 'currentLogFile.txt', 'a')
    except:
        pass
    while True:
        currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
        activeUsers = get_active_users()
        print(str(currentTime) + 'Subscribers: ' + str(subToWatch.subscribers) + ' | Active Users: ' + str(activeUsers))
        subLogFile.write(str(currentTime) + str(subToWatch.subscribers) + '\n')
        currentLogFile.write(str(currentTime) + str(activeUsers) + '\n')
        time.sleep(WAIT_TIME * 60)

if __name__ == "__main__":
	main()
