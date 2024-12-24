"""standard freeze script"""

from flask_flatpages import FlatPages
from flask_frozen import Freezer

# instead of "filename," below, use the name of the file that
# runs YOUR Flask app - omit .py from the filename
from app import app


app.config['subdomain_matching'] = False    
#app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)
pages = FlatPages(app)

@freezer.register_generator
def year():
    posts =  [page for page in pages if 'date' in page.meta]
    def article_year(articles):
        art_list = []
        for artcile in articles:
            art_list.append(str(artcile.meta['date'])[0:4])
        return list(set(art_list))
    art_year = sorted(article_year(posts), reverse=True)

    for product in art_year:
        yield 'year', {'year': product}

app.config['FREEZER_DESTINATION'] = "../leyouz233"

if __name__ == '__main__':
    freezer.freeze()
    print("冻结结束")
