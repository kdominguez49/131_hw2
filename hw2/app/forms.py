from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField 
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    #add
    # author (string) validator should make this textbox required
    author=StringField('Author', validators=[DataRequired()])
    # message (string) validator should make this textbox required
    message=StringField('Message', validators=[DataRequired()])
    # submit (button) text should say 'Send' 
    submit= SubmitField('Send')
