from flask import Blueprint


bp = Blueprint('site', __name__)

@bp.app_template_global()
def get_page_div(page, request_page, *args):
    """Creates a div element for a page and sets the requested page visible""" 
    classes = "".join([arg for arg in args])
    params = (page, classes)
    params += ('style="display:block"',) if request_page == page else ('',)
    return '<div id="%s" class="page %s" %s>' % param