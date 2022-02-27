from flask import render_template
from app import app
from app.models import news_sources, news_articles
from .request import get_sources, get_articles

#views
@app.route('/')
def index():

    '''
    view root page function that returns index page
    '''

    #get news sources
    news_sources = get_sources()
    

    title = 'Newsfetch - All your news in one place'

    return render_template('index.html', title = title, source = news_sources)


@app.route('/<string:id>')
def article(id):

    '''
    View articles page function that returns a list of articles from the news source
    '''
    news_articles = get_articles(id)
    id = id
    #title = f'{news_articles.title}'
    print("testing", id)
  

    return render_template('sources.html', article = news_articles, source = id)