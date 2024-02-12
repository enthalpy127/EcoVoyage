from wtforms import Form, StringField, SelectField, validators, IntegerField
from wtforms.fields import EmailField


class CreateOrderForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    phone = IntegerField('Phone Number', [validators.Length(min=1, max=10), validators.DataRequired()])
    destination = SelectField('Destination', [validators.DataRequired()], choices=[('', 'Select'), ('Garden by the bay', 'Garden by the bay'),
                                                                                   ('Botanic Gardens', 'Botanic Gardens'), ('Singapore Zoo', 'Singapore Zoo'),
                                                                                   ('Universal Studios', 'Universal Studios'), ('S.E.A Aquarium', 'S.E.A Aquarium'),
                                                                                   ('Givskud Zoo Zootopia', 'Givskud Zoo Zootopia'), ('The Ancient Viking Stronghold of Aros', 'The Ancient Viking Stronghold of Aros'),
                                                                                   ('Tour with Odense River Cruise', 'Tour with Odense River Cruise'), ('Street Art and Rooftops of Aarhus', 'Street Art and Rooftops of Aarhus'),
                                                                                   ('SUP - Stand Up Paddle - Kitesurfing - Wingfoil & Kitefoil courses', 'SUP - Stand Up Paddle - Kitesurfing - Wingfoil & Kitefoil courses'),
                                                                                   ('Explore the Instaworthy Spots of Aarhus with a Local', 'Explore the Instaworthy Spots of Aarhus with a Local'),
                                                                                   ('Swiss National Park & Ofenpass Area Nature Trail', 'Swiss National Park & Ofenpass Area Nature Trail'),
                                                                                   ('Mount Rigi', 'Mount Rigi'), ('Luke Lucerne Lake', 'Luke Lucerne Lake'),
                                                                                   ('Mount Pilatus Summit', 'Mount Pilatus Summit'),
                                                                                   ('Similan Islands', 'Similan Islands'),
                                                                                   ('Charuchak Park', 'Charuchak Park'),
                                                                                   ('Bangkok Butterfly Garden and Insectarium', 'Bangkok Butterfly Garden and Insectarium'),
                                                                                   ('Erawan Waterfall', 'Erawan Waterfall'),
                                                                                   ('Bamboo Bicycle Tour in twilight', 'Bamboo Bicycle Tour in twilight'),
                                                                                   ('Temple of the Golden Buddha', 'Temple of the Golden Buddha')],
    default='')
    number_of_adult_ticket = SelectField('Number of adult ticket', [validators.DataRequired()], choices=[('1', '1'),
                                                                                   ('2', '2'), ('3', '3'),
                                                                                   ('4', '4'), ('5', '5'),
                                                                                   ('6', '6'), ('7', '7'),
                                                                                   ('8', '8'), ('9', '9'),
                                                                                   ('10', '10'),('11', '12'),
                                                                                   ('13', '13'),
                                                                                   ('14', '14'), ('15', '15'),
                                                                                   ('16', '16'), ('17', '17'),
                                                                                   ('18', '18'), ('19', '19'),
                                                                                   ('20', '20')],
    default='')
    number_of_child_ticket = SelectField('Number of child ticket', [validators.DataRequired()], choices=[('0', '0'), ('1', '1'),
                                                                                   ('2', '2'), ('3', '3'),
                                                                                   ('4', '4'), ('5', '5'),
                                                                                   ('6', '6'), ('7', '7'),
                                                                                   ('8', '8'), ('9', '9'),
                                                                                   ('10', '10'),('11', '11'),
                                                                                   ('12', '12'), ('13', '13'),
                                                                                   ('14', '14'), ('15', '15'),
                                                                                   ('16', '16'), ('17', '17'),
                                                                                   ('18', '18'), ('19', '19'),
                                                                                   ('20', '20'),('21', '21'),
                                                                                   ('22', '22'), ('23', '23'),
                                                                                   ('24', '24'), ('25', '25'),
                                                                                   ('26', '26'), ('27', '27'),
                                                                                   ('28', '28'), ('29', '29'),
                                                                                   ('30', '30')],
    default='')

