#!/usr/bin/python3
""" returns the number of subscribers for a given subreddit """
import re
import requests
def number_of_subscribers(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/about/"
    res = requests.get(url)
    html = res.text
    pattern = r'subscribers="([^"]*)"'
    subscribers = re.search(pattern, html)

    if subscribers:
        return int(subscribers[0][13:-1])
    else:
        return 0
