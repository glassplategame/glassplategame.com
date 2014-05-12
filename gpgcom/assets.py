from flask.ext.assets import Bundle

from flask_spirits.assets import js_jquery, js_bootstrap, css_bootstrap

js_public = Bundle(
    js_jquery,
    js_bootstrap
)

css_public = Bundle(
    css_bootstrap,
    'css/gpg.css'
)

js_admin = Bundle()

css_admin = Bundle()