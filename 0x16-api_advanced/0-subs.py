#!/bin/usr/python3
""" function that queries the Reddit API
and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0

    d = res.json().get('data')
    return d['subscribers']
