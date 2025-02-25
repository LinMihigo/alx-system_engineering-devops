#!/usr/bin/python3
"""
Contains functions that queries reddit api
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the the first 10 host posts on a specified subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom-script/1.0"}
    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
