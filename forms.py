from flask_wtf import FlaskForm #pip install flask-wtf
from wtforms import StringField, SelectField, SubmitField

class DefectForm(FlaskForm):
    mail = StringField('Please enter your email adress')
    name = StringField('Name')
    role = StringField('Which role describes you best?')
    organization = StringField('What is the name of your organization?')
    deviceID = StringField('What is your device ID?')
    date = StringField('When did the bug occur?')
    comment =SelectField(u'What would you like to comment on?', choices=
    [('User Manual', 'User Manual'),
    ('Guardian Earbuds','Guardian Earbuds'),
    ('IDUN Python SDK','IDUN Python SDK'),
    ('IDUN Cloud','IDUN Cloud'),
    ('Acquierd signal', 'Acquierd signal'),
    ('Other', 'Other')])
    bugTitle = StringField('Give your bug a short title/name?')
    busDesc = StringField('Desribe your bug (device, browser, oerating system, settings, etc.)?')
    reproduction = SelectField(u'Were you able to reproduce the bug?', choices=[('1','yes'), ('0','no')])
    version = StringField('Which version are you using (Pyhton SDK 0.12, WebApp 0.1 etc.)?')
    #optional upload...
    submit = SubmitField('Submit bug')
