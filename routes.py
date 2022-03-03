"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/im_phot')
@view('im_phot')
def about():
    
    return dict(
        title='I am a photographer',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/prices')
@view('prices')
def prices():
    """Renders the about page."""
    return dict(
        title='PRICE LIST',
        message='Your application description page.',
        year=datetime.now().year
    )
