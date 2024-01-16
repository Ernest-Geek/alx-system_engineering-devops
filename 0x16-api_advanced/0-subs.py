#!/usr/bin/python3
"""
Get the number of subscribers for a given subreddit using the Reddit API.
"""

import sys
import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for getting subreddit information
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Make the GET request
    response = requests.get(api_url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        # Return the extracted number of subscribers
        return subscribers
    else:
        # If an invalid subreddit is given or there is an issue with the request
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./get_subscribers.py subreddit_name")
        sys.exit(1)

    subreddit_name = sys.argv[1]

    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"The subreddit {subreddit_name} has {subscribers_count} subscribers.")

