from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)


@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    del posts[0]
    sorted_posts = sorted(posts, reverse=True,
                          key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts)


@app.route('/article/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


if __name__ == '__main__':
    app.run()
