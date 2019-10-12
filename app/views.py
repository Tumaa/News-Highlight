from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@app.route('/articles/<articles_id>')
def articles(articles_id):

    '''
    View movie page function that returns the articles details page and its data
    '''
    return render_template('articles.html',id = articles_id)
