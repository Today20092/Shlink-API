import sys
import requests
import pyperclip
import creds 

def shorten_url(long_url):
    # Shlink API base URL 
    base_url = creds.base_url

    # Replace 'your-api-key' with your actual API key/token
    api_key = creds.api_key

    # Data for creating short URL
    # Change the tag to something identifiable for you
    data = {
        "longUrl": long_url,
        "tags": ["Windows 11 API Keyboard Shortcut"],
        "crawlable": False,
        "forwardQuery": True,
        "findIfExists": True,
        "domain": creds.domain,
        "shortCodeLength": 7
    }

    # Headers including API key
    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    try:
        # Make POST request to create short URL
        response = requests.post(base_url, json=data, headers=headers)
        
        # Check if request was successful
        if response.status_code == 200:
            # Extract short URL from response
            short_url = response.json()['shortUrl']
            pyperclip.copy(short_url)
            print(short_url)
        else:
            print(f'Failed to create short URL. Status code: {response.status_code}')
            print(response.text)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]
    shorten_url(url)
