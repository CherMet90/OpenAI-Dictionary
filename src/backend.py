from flask import Flask, request, render_template
import requests
import json
from functools import lru_cache
import os

app = Flask(__name__)

GIPHY_API_KEY = os.environ.get('GIPHY_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

@lru_cache(maxsize=128)  # Cache up to 128 most recent requests
def get_giphy_url(word):
    # Remove space from the end of the word
    word = word.strip()
    if ' ' in word:
        return None
    response = requests.get(
        f'https://api.giphy.com/v1/gifs/search?q={word}&api_key={GIPHY_API_KEY}&limit=1'
    )
    response_data = response.json()
    if response_data['data']:
        gif_url = response_data['data'][0]['images']['original']['url']
        return gif_url
    else:
        return None

print(get_giphy_url.cache_info())

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_definition', methods=['POST'])
def get_definition():
    sentence = request.form['sample-sentence']
    word = request.form['word']
    definition = get_gpt_definition(sentence, word)
    gif_url = get_giphy_url(word)
    return render_template('definition.html', definition=definition, gif_url=gif_url, word=word)

def get_gpt_definition(sentence, word):
    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        },
        json={
            "prompt": f"Imagine you are my tutor. I learn english on B1 level.'{sentence}'. Explain meaning of the '{word}' in that phrase, please, and provide more common synonyms. If '{word}' is verb, show infinitive of it. If it's plural noun - provide singular form.",
            "model": 'text-davinci-002',
            "max_tokens": 500,
            "temperature": 0.5,
            "n": 1
        }
    )
    response_data = response.json()
    definition = response_data['choices'][0]['text'].strip()
    return definition

if __name__ == '__main__':
    app.run(debug=True)
