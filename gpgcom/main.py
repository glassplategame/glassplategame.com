from datetime import datetime as dt

from flask import g, Flask, render_template, session, request, redirect, \
    current_app, flash, url_for, abort, Markup
from flask.ext.assets import Environment
from flask.ext.login import current_user
from flask.ext.mail import Message, Mail
from flask.ext.restless import APIManager
from flask.ext.restless import ProcessingException
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf.csrf import CsrfProtect

from flask_spirits import FlaskSpirits
from flask_spirits.controllers import user
from flask_spirits.database import session as db_session

from gpgcom.assets import js_public, css_public, js_admin, css_admin
from gpgcom.controllers import admin
from gpgcom.forms import GameForm, ContactForm
from gpgcom.models import Game


# Create Flask Instance
app = Flask(__name__, static_folder='../static', template_folder='../jinja')

# Configure App
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

FlaskSpirits(app, email_on_error=app.config['MAIL_ERROR'])

# Load controllers
app.register_blueprint(user.bp)

# Debug toolbar
toolbar = DebugToolbarExtension(app)

# Set up CSRF protection
csrf = CsrfProtect()
csrf.init_app(app)

# Set up Mail
mail = Mail(app)

# Set up JS/CSS assets
assets = Environment(app)    
assets.register('js_public', js_public)
assets.register('css_public', css_public)
assets.register('js_admin', js_admin)
assets.register('css_admin', css_admin)

# API
def check_api_auth(**kw):
    if not current_user.is_authenticated():
        raise ProcessingException(description='Not authenticated!', code=401)
    return True

def post_get_single(result=None, **kw):
    if result:
        result['start'] = dt.strptime(result['start'], '%Y-%m-%dT%H:%M:%S') \
                            .strftime('%m/%d/%Y %H:%M:%S')
        if result['end']:
            result['end'] = dt.strptime(result['end'], '%Y-%m-%dT%H:%M:%S') \
                              .strftime('%m/%d/%Y %H:%M:%S')

restless = APIManager(app, session=db_session)
restless.create_api(Game, 
                    methods=['GET', 'POST', 'DELETE', 'PATCH'],
                    preprocessors=dict(
                        GET_SINGLE=[check_api_auth],
                        GET_MANY=[check_api_auth],
                        PATCH_SINGLE=[check_api_auth],
                        POST_SINGLE=[check_api_auth]
                    ),
                    postprocessors=dict(
                        GET_SINGLE=[post_get_single]
                        )
                    )

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
        page=path[0] if path[0] in pages else 'home',
        contact_form=ContactForm(prefix='contact'),
        game_form=GameForm(prefix='game'),
        games=Game.current_playings())

    return render_template('index.jinja', **jinja_var)

@app.route('/contact', methods=['POST'])
def contact():
    form = ContactForm(request.form, prefix='contact_')
    if not form.validate():
        flash('Failed to send message', 'alert')
        errors = {}
        for error in form.errors:
            errors['contact_' + error] = form.errors[error]
        session['contact_form_errors'] = errors
        return redirect('/contact')
    
    data = (form.data['name'], form.data['email'], form.data['message'])
    msg = Message('New Message from glassplategame.com',
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=app.config['MAIL_CONTACT'],
        html="From: %s<br/>Email: %s<br/>Message: %s<br/>" % data,
        body="From: %s\r\nEmail: %s\r\nMessage: %s\r\n" % data)
    mail.send(msg)
    flash('Message sent successfully!', 'alert')
    return redirect('/')