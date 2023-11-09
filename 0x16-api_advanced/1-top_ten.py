#!/usr/bin/python3
'''This function queries the Reddit API
and prints the titles of the first
10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    '''top 10 hot posts listed'''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Python/requests"
        }
    params = {
        "limit": 10
        }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code in [302, 404]:
        print("None")
    else:
        results = response.json().get("data", {}).get("children", [])
        for post in results:
            post_data = post.get("data", {})
            title = post_data.get("title")
            if title:
                print(title)
