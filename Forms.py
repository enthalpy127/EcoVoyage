from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],
    default='')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CustomerLoginForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=30), validators.DataRequired()])
    password = StringField('Password', [validators.Length(min=10, max=10), validators.DataRequired()])
    logout = StringField('logout')
    changelogin = StringField('changelogin')

class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    username = StringField('Username', [validators.Length(min=3, max=30),validators.DataRequired()])
    password = StringField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    birthday = DateField('Birthday', format='%Y-%m-%d')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])

