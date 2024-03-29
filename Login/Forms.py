from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, IntegerField
from wtforms.fields import EmailField, DateField
from wtforms.validators import NumberRange


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=2, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=2, max=150), validators.DataRequired()])
    username = StringField('Username',[validators.Length(min=3, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],
    default='')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
    password = StringField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])

class CustomerLoginForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=30), validators.DataRequired()])
    password = StringField('Password', [validators.Length(min=10, max=10), validators.DataRequired()])
    changelogin = StringField('changelogin')
    logout = StringField('logout')

class CreateCustomerForm(Form):
    username = StringField('User Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    birthday = DateField('Birthday', format='%Y-%m-%d')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
    password = StringField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])

class CreateFeedbackForm(Form):
    name = StringField('name', [validators.Length(min=1, max=150), validators.DataRequired()])
    star_rating = IntegerField('star_rating', validators=[NumberRange(min=1, max=5, message='Range Error')])
    title = StringField('title', [validators.Length(min=1, max=150), validators.DataRequired()])
    message = TextAreaField('message', [validators.length(max=200), validators.DataRequired()])
    date_submitted = DateField('date_submitted', format='%Y-%m-%d')
