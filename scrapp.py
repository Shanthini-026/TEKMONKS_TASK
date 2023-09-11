import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify,render_template

app = Flask(__name__)

@app.route('/getTimeStories')
def index():
    response = requests.get('https://time.com/')
    soup = BeautifulSoup(response.content, 'html.parser')
    latest_stories_section = soup.find('div', {'class': 'partial latest-stories'})
    stories = latest_stories_section.find_all('a')
    latest_stories = [{'title': story.text, 'link': "https://time.com"+story['href']} for story in stories]
    return jsonify(latest_stories)
@app.route('/')
def content():
    response = requests.get('https://time.com/')
    soup = BeautifulSoup(response.content, 'html.parser')
    latest_stories_section = soup.find('div', {'class': 'partial latest-stories'})
    stories = latest_stories_section.find_all('a')
    latest_stories = [{'title': story.text, 'link':"https://time.com"+ story['href']} for story in stories]
    return render_template('index.html',latest_stories=latest_stories)

if __name__ == '__main__':
    app.run()

