#!/usr/bin/python3
"""Contains functions that queries reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries reddit api recursively and returns a list containing the tiles of
    all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom-script/1.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])

    hot_list.extend([post["data"]["title"] for post in posts])

    after = data.get("after")
    return recurse(subreddit, hot_list, after) if after else hot_list
