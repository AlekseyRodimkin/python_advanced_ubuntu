from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired('Empty email'), Email()])
    phone = IntegerField(validators=[InputRequired('Empty phone'), NumberRange(min=1000000000, max=9999999999)])
    name = StringField(validators=[InputRequired('Empty name')])
    surname = StringField(validators=[InputRequired('Empty surname')])
    address = StringField(validators=[InputRequired('Empty address')])
    index = IntegerField()
    comment = StringField()


class LuckyTicketForm(FlaskForm):
    name = StringField(validators=[InputRequired('Empty name')])
    family_name = StringField(validators=[InputRequired('Empty family name')])
    ticket_number = IntegerField(validators=[InputRequired('Empty ticket number'), NumberRange(min=100000, max=999999)])


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        return f"Successfully registered user {email} with phone +7{phone}"
    return f"Invalid input, {form.errors}", 400


@app.route("/luckyticket", methods=["POST"])
def lucky_ticket():
    form = LuckyTicketForm()

    if form.validate_on_submit():
        name, family_name, ticket_number = form.name.data, form.family_name.data, form.ticket_number.data
        first_half, second_half = 0, 0
        for i_num in range(3):
            first_half += int(str(ticket_number)[i_num])
            second_half += int(str(ticket_number)[i_num + 3])

        if first_half == second_half:
            return f"Поздравляем вас, {name} {family_name}, ticket number {ticket_number} WON"
        return "Неудача. Попробуйте ещё раз!"
    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
