import requests
from bs4 import BeautifulSoup
import gtts
from playsound import playsound

page = requests.get("https://www.dictionary.com/e/word-of-the-day/")
soup = BeautifulSoup(page.content, 'html.parser')

word = str(soup.find_all('h1', {'class': 'js-fit-text'})).split(">")[1].split("<")[0]
definition = str(soup.find_all('div', {'class': 'otd-item-headword__pos'})).split("<p>")[2].split("<")[0]

tts = gtts.gTTS(word)
tts.save("word.mp3")

tts = gtts.gTTS(definition)
tts.save("definition.mp3")

playsound("word.mp3")
playsound("definition.mp3")

