from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, URL, NumberRange
from flask_bootstrap import Bootstrap
from FindContacts import *

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"


class SearchForm(FlaskForm):
    search_string = StringField(label="Query", validators=[DataRequired()])
    number_of_contacts = IntegerField(label="Number Of Results", validators=[DataRequired(), NumberRange()])
    submit = SubmitField("Search")


@app.route('/', methods=['GET', 'POST'])
def home():
    my_form = SearchForm()
    if my_form.validate_on_submit():
        return redirect(url_for("loading",target=my_form.number_of_contacts.data,keyword=my_form.search_string.data))
    return render_template("home.html", form=my_form)


@app.route('/searching/<keyword>/<target>', methods=['GET', 'POST'])
def loading(keyword, target):
    page_number = 1
    while len(numbers) < int(target):
        keyword.replace("", "-")
        start_collecting(keyword, page_number)
        page_number += 1
        DataFrame(numbers).to_csv("static/files/humans.csv")
    return render_template("download.html")


@app.route('/download')
def send_file():
    return send_from_directory("static/files/", filename='humans.csv')


if __name__ == '__main__':
    app.run(debug=True)
