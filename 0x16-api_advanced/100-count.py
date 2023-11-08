#!/usr/bin/python3
"""requests module"""
import requests


def count_words(subreddit, word_list, after=None, dic=None):
    """ returns a list containing the titles of all hot articles"""

    if dic is None:
        dic = {word: 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    res = requests.get(url, headers={'User-Agent': 'abeer'})

    if res.status_code != 200:
        return

    hot = res.json()
    for article in hot['data']['children']:
        for word in word_list:
            if f" {word.lower()} " in article['data']['title'].lower():
                dic[word] += 1

    after = hot['data']['after']
    if not after:
        print(dic)
        sorted_dict = dict(sorted(dic.items()))
        for key, value in sorted_dict.items():
            if value:
                print(f"{key}: {value}")
        return

    return (count_words(subreddit, word_list, after, dic))
