#!/usr/bin/python3
'''
The recursive function queries the Reddit API
and returns a list containing the titles of
all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''This function recursively queries the
    reddit API for hot articles'''

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
        "limit": 100,
        "after": after
    }
    headers = {
            "User-Agent": "Python/requests"
    }
    results = requests.get(url, params=params,
                           headers=headers, allow_redirects=False)
    if results == 200:
        data = response.json()
        hot_posts = results.get('data').get('children')
        after = results.get('data').get('after')
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
