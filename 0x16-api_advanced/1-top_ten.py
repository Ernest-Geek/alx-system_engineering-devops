import sys
import requests


def top_ten(subreddit):
    # Reddit API endpoint for getting hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        # Make the GET request
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        # Parse the JSON response and extract post titles
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Print the titles of the first 10 hot posts
        for post in posts:
            title = post['data'].get('title', '')
            print(title)

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(None)
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as value_err:
        print(f"ValueError occurred (JSON decoding error): {value_err}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./get_top_posts.py subreddit_name")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    top_ten(subreddit_name)
