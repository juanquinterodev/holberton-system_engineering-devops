#!/usr/bin/python3
"""
    top ten
"""
import requests


def top_ten(subreddit):
    """
        prints the first 10 hot posts
        @subreddit: suscriptors
    """
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    request = requests.get(url, headers=header, allow_redirects=False)

    if request.status_code != 200:
        print(None)
        return
    jsonreq = request.json()

    if 'data' in jsonreq:
        for top in jsonreq.get("data").get("children"):
            print(top.get("data").get("title"))
    else:
        print(None)
