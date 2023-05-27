import wtforms
from flask_wtf import FlaskForm

class AddBooks(FlaskForm):
    name = wtforms.StringField('Book Name', [wtforms.validators.DataRequired()])
    author = wtforms.StringField('Book Author', [wtforms.validators.DataRequired()])
    rating = wtforms.DecimalField('Rating', [wtforms.validators.DataRequired(), wtforms.validators.NumberRange(0, 10) ])
    submit = wtforms.SubmitField('Add')
    
    
    