### Script to get the classical song to be displayed in the app. 
import requests
import webbrowser


# Log into Reddit API and extract data from r/classicalmusic
use_script = "cdr2bF4x6u-OevHkrylIlA"
secret = "Qwbm2Vwef_EbqBMUuaYZcwN5kK5m7w"

auth = requests.auth.HTTPBasicAuth(use_script, secret)

data = {'grant_type': 'password',
        'username': 'hamiltonewan1',
        'password': 'Smudge01'}

headers = {'User-Agent': 'daily_song/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get("https://oauth.reddit.com/r/classicalmusic/hot",
                   headers=headers)

# Get the hyperlinks from all the posts. 
links = []
for post in res.json()['data']['children']:
    links.append(post['data']['url'])

# Filter the hyperinks to only get YouTube links and then choose the first one. 
yt_links = []
key = 'youtu'
for link in links:
    if key in link:
        yt_links.append(link)

video = yt_links[0]

# Open the YouTube video in webbrowser.
webbrowser.open(video)



