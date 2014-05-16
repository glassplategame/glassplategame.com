from flask.ext.assets import Bundle

from flask_spirits.assets import js_jquery, js_bootstrap, css_bootstrap, \
    js_davis, js_lodash, js_alertify, css_alertify

js_public = Bundle(
    js_jquery,
    js_bootstrap,
    js_alertify,
    js_davis,
    js_lodash,
    'js/gpg.js'
)

css_public = Bundle(
    css_bootstrap,
    css_alertify,
    'css/gpg.css'
)

js_admin = Bundle()

css_admin = Bundle()