from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    general_news = get_news_sources('general')
    business_news = get_news_sources('business')
    entertainment_news = get_news_sources('entertainment')
    sports_news = get_news_sources('sports')
    technology_news = get_news_sources('technology')

    title = 'Homepage'

@app.route('/articles/<articles_id>')
def articles(articles_id):

    '''
    View news page function that returns the articles details page and its data
    '''
    return render_template('articles.html',id = articles_id)
