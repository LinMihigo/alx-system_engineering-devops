#!/usr/bin/python3
"""
Contains functions that queries reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries reddit api and returns number of subscribers of a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-script/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)

    return 0
