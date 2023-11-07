#!/usr/bin/python3
'''The function queries the Reddit API and returns
the number of subscribers (not active users,
total subscribers) for a given subreddit.
If an invalid subreddit is given,
the function should return 0.
'''

import requests


def number_of_subscribers(subreddit):
    '''gets the number of subscribers'''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        results = response.json().get("data")
        return results.get("subscribers")
