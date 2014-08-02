from wtforms.form import Form
from wtforms_alchemy import ModelForm


class PlayingForm(ModelForm):
    class Meta:
        model = Playing
