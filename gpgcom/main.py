from flask import g, Flask, render_template, session, request, redirect, \
    current_app, flash, url_for, abort, Markup
from flask.ext.assets import Environment
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf.csrf import CsrfProtect

from flask_spirits import FlaskSpirits
from flask_spirits.controllers import user

from gpgcom.assets import js_public, css_public, js_admin, css_admin
from gpgcom.controllers import site


# Create Flask Instance
app = Flask(__name__, static_folder='../static', template_folder='../jinja')

# Configure App
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

FlaskSpirits(app, email_on_error=app.config['MAIL_ERROR'])

# Load controllers
app.register_blueprint(site.bp, url_prefix='/api')
app.register_blueprint(user.bp)

# Debug toolbar
toolbar = DebugToolbarExtension(app)

# Set up CSRF protection
csrf = CsrfProtect()
csrf.init_app(app)

# Set up JS/CSS assets
assets = Environment(app)    
assets.register('js_public', js_public)
assets.register('css_public', css_public)
assets.register('js_admin', js_admin)
assets.register('css_admin', css_admin)

@app.template_global()
def get_page_div(page, request_page, *args):
    'Creates a div element for a page and sets the requested page visible' 
    classes = "".join([arg for arg in args])
    params = (page, classes)
    params += ('style="display:block"',) if request_page == page else ('',)
    return '<div id="%s" class="page %s" %s>' % params

@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    'Main controller of website'

    path = path.split('/') if path else ['home']

    # Facebook Scraper
    if (request.user_agent.string.lower().find('facebookexternalhit') > -1 or
        '_debug_facebook_scrape_' in request.args):
        return facebook.scrape(path)

    pages = ['about', 
             'playing_the_game', 
             'current_playing', 
             'cards', 
             'contact', 
             'links' ]

    # These pages require loading something
    ajax_pages = []

    # Public template variables
    jinja_var = dict(
        page=path[0] if path[0] in pages else 'home')

    return render_template('index.jinja', **jinja_var)

