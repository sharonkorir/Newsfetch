from flask import render_template
from app import app
from .request import get_sources

#views
@app.route('/')
def index():

    '''
    view root page function that returns index page
    '''

    #get news sources
    news_sources = get_sources()
    print(news_sources)
    title = 'Newsfetch - All your news in one place'
    return render_template('index.html', title = title, source = news_sources)