def number_of_subscribers(subreddit):
    from urllib import request
    import re

    url = f"https://www.reddit.com/r/{subreddit}/about/"
    res = request.urlopen(url)
    html = res.read().decode('utf-8')
    pattern = r'subscribers="([^"]*)"'
    subscribers = re.search(pattern, html)

    if subscribers:
        return int(subscribers[0][13:-1])
    else:
        return 0
