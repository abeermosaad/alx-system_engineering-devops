#!/usr/bin/python3
"""requests module"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns a list containing the titles of all hot articles"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    res = requests.get(url, headers={'User-Agent': 'abeer'})

    if res.status_code != 200:
        return None

    hot = res.json()

    for article in hot['data']['children']:
        hot_list.append(article['data']['title'])

    if not hot['data']['after']:
        return hot_list

    after = hot['data']['after']

    return (recurse(subreddit, hot_list, after))
