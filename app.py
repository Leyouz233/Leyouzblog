from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    posts =  [page for page in pages if 'date' in page.meta]
    def article_year(articles):
        art_list = []
        for artcile in articles:
            art_list.append(str(artcile.meta['date'])[0:4])
        return list(set(art_list))
    art_year = sorted(article_year(posts), reverse=True)

    sorted_posts = sorted(posts, reverse=True,                                                         key=lambda page: page.meta['date'])
    new_article = sorted_posts[0]

    return render_template('index.html', years=art_year, new_page=new_article)

@app.route('/<year>.html')
def year(year):
    posts =  [page for page in pages if 'date' in page.meta]
    def article_year(articles):
        art_list = []
        for artcile in articles:
            if str(year) in str(artcile.meta['date']):
                art_list.append(str(artcile.meta['date'])[5:7])
        return list(set(art_list))
    art_mon = sorted(article_year(posts), reverse=True)

    sorted_posts = sorted(posts, reverse=True,                                                         key=lambda page: page.meta['date'])
    new_article = sorted_posts[0]

    return render_template('year.html', year=year, months=art_mon, new_page=new_article)

@app.route('/<year>/<month>.html')
def month(year, month):
    posts = [page for page in pages if 'date' in page.meta and 'top' not in page.meta]
    new_posts = []

    for post in posts:
        yeardate = str(post.meta['date'])[0:4]
        monthdate = str(post.meta['date'])[5:7]

        if str(year) == yeardate and str(month) == monthdate:
            new_posts.append(post)

    top_articles = [page for page in pages if 'date' in page.meta]
    def top_article(articles):
        for article in articles:
            if 'top' in article.meta:
                return article

    sorted_posts = sorted(new_posts, reverse=True,
                          key=lambda page: page.meta['date'])

    return render_template('month.html', month=month, top_page=top_article(top_articles), pages=sorted_posts)

'''
@app.route('/main.html', methods=['GET', 'POST'])
def main():
    posts = [page for page in pages if 'date' in page.meta and 'top' not in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
                          key=lambda page: page.meta['date'])


    top_articles = [page for page in pages if 'date' in page.meta]

    def top_article(articles):
        for article in articles:
            if 'top' in article.meta:
                return article

    return render_template('main.html', top_page=top_article(top_articles), pages=sorted_posts)
'''

@app.route('/about.html')
def about():
    facker_about = pages.get('about')
    return render_template('page.html', page=facker_about)


@app.route('/article/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
