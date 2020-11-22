from flask import render_template
from app import app

# Views
@app.route('/')
def home():

    '''
    View root page function that returns the home page and its data
    '''
    message = 'Hello World'
    return render_template('home.html',message = message)

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('news.html',id =news_id)