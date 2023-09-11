import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getTimeStories')
def index():
    response = requests.get('https://time.com/')
    soup = BeautifulSoup(response.content, 'html.parser')
    latest_stories_section = soup.find('div', {'class': 'partial latest-stories'})
    stories = latest_stories_section.find_all('a')
    latest_stories = [{'title': story.text, 'link': story['href']} for story in stories]
    return jsonify(latest_stories)

if __name__ == '__main__':
    app.run()

