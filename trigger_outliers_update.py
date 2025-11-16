import os
import sys
import requests

OUTLIERS_HOST = os.getenv("OUTLIERS_HOST")
OUTLIERS_PORT = "9090" 
API_URL = f"http://{OUTLIERS_HOST}:{OUTLIERS_PORT}/api/update"
API_KEY = os.getenv("OUTLIERS_API_KEY")

payload = {
    "title": ["Wiki Pageviews", "Wiki Pageviews Projects"]
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def main():
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        sys.exit(f"HTTP {response.status_code} error: {response.text}")
    except Exception as e:
        sys.exit(f"Request error: {e}")

    data = None
    try:
        data = response.json()
    except ValueError:
        sys.exit(response.text)

    print(data)

if __name__ == "__main__":
    main()
