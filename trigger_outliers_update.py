import os
import requests

OUTLIERS_HOST = os.getenv("OUTLIERS_HOST") 
API_URL = f"{OUTLIERS_HOST}/api/update"
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
        print(f"HTTP {response.status_code} error:")
        print(response.text.strip())
        return
    except Exception as e:
        print(f"Request error: {e}")
        return

    data = None
    try:
        data = response.json()
    except ValueError:
        print(response.text.strip())
        return

    print(data)

if __name__ == "__main__":
    main()
