#!/usr/bin/python3
"""returns number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    head = {"User-Agent": "Client"}
    request = requests.get(url, headers=head)
    if request.status_code != 200:
        return 0
    return request.json().get("data").get("subscribers")
