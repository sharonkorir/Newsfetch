from flask import render_template
from app import app

#views
@app.route('/')
def index():

    '''
    view root page function that returns index page
    '''

    title = 'Newsfetch - All your news in one place'
    return render_template('index.html', title = title)