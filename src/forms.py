from flask_wtf import FlaskForm
from wtforms import DateTimeField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange


class TaxiShareForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired()])
    phone_number = IntegerField(
        "Phone Number",
        validators=[DataRequired(), NumberRange(
            min=1000000000, max=9999999999)],
    )
    email = StringField("Enter your Email", validators=[
                        DataRequired(), Email()])
    start_location = StringField(
        " Start Location", validators=[DataRequired()])
    end_location = StringField("End Location", validators=[DataRequired()])

    date_time = DateTimeField(
        "Enter Date And Time for Trip",
        format="%Y-%m-%dT%H:%M",
        validators=[DataRequired()],
        render_kw={"placeholder": "YYYY-MM-DD HH:MM",
                   "type": "datetime-local"},
    )

    available_seats = IntegerField(
        "Enter Number of seats", validators=[DataRequired()])
    price_per_seat = IntegerField(
        "Enter Price of seats", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    phone_number = IntegerField(
        "Phone Number",
        validators=[DataRequired(), NumberRange(
            min=1000000000, max=9999999999)],
    )
    email = StringField("Enter your Email", validators=[
                        DataRequired(), Email()])
    submit = SubmitField("Add User")
