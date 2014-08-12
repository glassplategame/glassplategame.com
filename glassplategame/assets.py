from flask.ext.assets import Bundle

from flask_spirits.assets import js_jquery, js_bootstrap, css_bootstrap, \
    js_davis, js_lodash, js_alertify, js_forms, css_alertify, css_modal, \
    css_forms, js_datetimepicker, css_datetimepicker

js_public = Bundle(
    js_jquery,
    js_bootstrap,
    js_datetimepicker,
    js_alertify,
    js_davis,
    js_lodash,

    js_forms,
    'js/gpg.js'
)

css_public = Bundle(
    css_bootstrap,
    css_datetimepicker,
    css_alertify,
    css_forms,
    css_modal,
    'css/gpg.css'
)

js_admin = Bundle()

css_admin = Bundle()