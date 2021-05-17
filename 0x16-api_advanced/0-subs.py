#!/usr/bin/python3
"""
Function that queries the Reddit API
"""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:\
                     v1.0.0 (by /u/vic9815)'}).json()
    sub_reddit = r.get('data', {}).get('subscribers', 0)
    return sub_reddit
