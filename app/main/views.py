from flask import render_template, request, redirect, url_for
from . import main
from app.models import Source, Article
from ..request import get_sources, get_articles, search_article

#views
@main.route('/')
def index():

    '''
    view root page function that returns index page
    '''

    #get news sources
    news_sources = get_sources()
    

    title = 'Newsfetch - All your news in one place'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search', article_title = search_article))
    else:
        return render_template('index.html', title = title, source = news_sources)


@main.route('/<string:id>')
def article(id):

    '''
    View articles page function that returns a list of articles from the news source
    '''
    news_articles = get_articles(id)
    id = id


    #title = f'{news_articles.title}'
  

    return render_template('articles.html', articles = news_articles, source = id)

@main.route('/search/<article_title>')
def search(article_title):

    '''
    View function to display search results
    '''

    article_title_list = article_title.split(" ")
    article_name_format = "+".join(article_title_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_title}'
    return render_template('search.html', articles = searched_articles)
