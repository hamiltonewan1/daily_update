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

res = requests.get("https://oauth.reddit.com/r/facts/hot",
                   headers=headers)
 
facts = []
for post in res.json()['data']['children']:
    facts.append(post['data']['title'])

fact = facts[0]

# Call text-to-speech.
tts = gtts.gTTS(fact)
tts.save("fact.mp3")
playsound("fact.mp3")

