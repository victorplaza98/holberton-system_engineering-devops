#!/usr/bin/python3
"""Function that queries the Reddit API"""


import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
    r = requests.get('http://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:\
                     v1.0.0 (by /u/vic9815))'},
                     params={'limit': 10}).json()
    inf = r.get('data', {}).get('children', None)
    if inf is None or (len(inf) > 0 and inf[0].get('kind') != 't3'):
        print(None)
    else:
        for i in inf:
            print(i.get('data', {}).get('title', None))
