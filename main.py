import sys
import requests
import json

def get_user_events(username):
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        event = response.json()
        print(json.dumps(event, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <github-username>")
    else:
        get_user_events(sys.argv[1])