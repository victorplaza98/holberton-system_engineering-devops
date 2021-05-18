#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    headers = headers = {'User-Agent': 'Python/requests:APIproject:\
                     v1.0.0 (by /u/vic9815)'}
    try:
        info = requests.get(url, headers=headers, allow_redirects=False).json()
        child = info.get('data').get('children')
        after = info.get('data').get('after')
        for i in child:
            hot_list.append(i.get('data').get('title'))
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except Exception:
        return None
