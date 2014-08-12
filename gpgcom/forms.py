from flask_wtf import Form
from wtforms import StringField 
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from gpgcom.models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ['updated_at']

class ContactForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Name')
    subject = StringField('Subject')
    message = TextAreaField('Message', validators=[DataRequired()])