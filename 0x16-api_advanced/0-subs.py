#!/bin/usr/python3
""" function that queries the Reddit API
and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/115.0.0.0 Safari/537.36"}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        res.raise_for_status()
    except res.exceptions.RequestException:
        return 0

    d = res.json()
    return d['data']['subscribers']
