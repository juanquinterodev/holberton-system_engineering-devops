#!/usr/bin/python3
from requests import get


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit"""
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    head = {'User-Agent': 'CustomClient/1.0'}
    request = requests.get(url, headers=header, allow_redirects=False)

    if request.status_code != 200:
        print(None)
        return
    json_req = request.json()

    if 'data' in jsonreq:
        for top in jsonreq.get("data").get("children"):
            print(top.get("data").get("title"))
    else:
        print(None)
