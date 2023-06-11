import wtforms
from flask_wtf import FlaskForm


class LogIn(FlaskForm):
    email = wtforms.EmailField(None, [wtforms.validators.DataRequired(), wtforms.validators.Email()], render_kw={"placeholder": "Email"})
    password = wtforms.PasswordField(None, [wtforms.validators.DataRequired()], render_kw={"placeholder": "Password"})
    submit = wtforms.SubmitField('Let me in')
    
    
class SignIn(FlaskForm):
    email = wtforms.EmailField(None, [wtforms.validators.DataRequired(), wtforms.validators.Email()], render_kw = {'placeholder': 'Email'})
    password = wtforms.PasswordField(None, [wtforms.validators.DataRequired()], render_kw = {'placeholder': 'Password'})
    name = wtforms.StringField(None, [wtforms.validators.DataRequired(), wtforms.validators.Length(1, 20)], render_kw = {'placeholder': 'Name'})
    submit = wtforms.SubmitField('Sign me up')
