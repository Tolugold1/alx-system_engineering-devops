#!/usr/bin/python3
"""
Query the Reddit API and return the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ prints the titles of the first 10 hot 
    posts listed for a given subreddit"""
    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                         format(subreddit),
                         headers={'User-Agent': 'custom'},
                         allow_redirects=False)
        for title in r.json().get('data').get('children'):
            print(title.get('data').get("title"))
    except:
        print(None)
