from wtforms.form import Form
from wtforms_alchemy import ModelForm

from gpgcom.models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ['updated_at']