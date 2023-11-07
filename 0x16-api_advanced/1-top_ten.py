#!/usr/bin/python3
"""request top ten posts of a subreddit"""
import requests


def top_ten(subreddit):
    """returns the top ten posts of a subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"
    res = requests.get(url, headers={'User-Agent': 'abeer'})

    if res.status_code != 200:
        print(None)
        return

    top = res.json()
    for post in top['data']['children']:
        print(post['data']['title'])
