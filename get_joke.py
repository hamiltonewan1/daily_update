### Script to get the joke to be displayed in the app. 

import requests
import webbrowser
import gtts
from playsound import playsound


# Log into Reddit API and extract data from r/jokes
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

res = requests.get("https://oauth.reddit.com/r/jokes/hot",
                   headers=headers)

# Get the setup and punchline for the joke. 
punchlines = []
setups = []
for post in res.json()['data']['children']:
    setups.append(post['data']['title'])
    punchlines.append(post['data']['selftext'])

setup = setups[2]
punchline = punchlines[2]

# Call text-to-speech.
tts = gtts.gTTS(setup)
tts.save("setup.mp3")

tts = gtts.gTTS(punchline)
tts.save("punchline.mp3")

playsound("setup.mp3")
playsound("punchline.mp3")

