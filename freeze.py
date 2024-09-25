"""standard freeze script"""

from flask_frozen import Freezer

# instead of "filename," below, use the name of the file that
# runs YOUR Flask app - omit .py from the filename
from app import app


app.config['subdomain_matching'] = False    
#app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)


app.config['FREEZER_DESTINATION'] = "leyouz233"

if __name__ == '__main__':
    freezer.freeze()
