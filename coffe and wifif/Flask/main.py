from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pandas
import wtforms

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = wtforms.URLField('cafe location on google maps (URL)',
                                [wtforms.validators.DataRequired(), wtforms.validators.URL()])
    opening_time = wtforms.TimeField('opening time', [wtforms.validators.DataRequired()])
    closing_time = wtforms.TimeField('closing time', [wtforms.validators.DataRequired()])
    coffee = wtforms.SelectField('coffee rating', [wtforms.validators.DataRequired()],
                                choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    power = wtforms.SelectField('power socket availability', [wtforms.validators.DataRequired()],
                               choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'] )
    wifi = wtforms.SelectField('wifi strength rating', [wtforms.validators.DataRequired()],
                                choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', encoding='utf-8') as csv_file:
            csv_file.write(f'''{form.cafe.data},{form.location.data},{form.opening_time.data},{form.closing_time.data},{form.coffee.data},{form.wifi.data},{form.power.data}\n''')
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
        return render_template('cafes.html', cafes=pandas.read_csv('cafe-data.csv', encoding = 'utf-8', header=None))


if __name__ == '__main__':
    app.run(debug=True)
