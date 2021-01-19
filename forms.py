from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TimeField, DateField, BooleanField, SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional
from wtforms_components import IntegerField


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])

class DeleteMeForm(FlaskForm):
    delacc = StringField()
    submit3 = SubmitField("submit")


class RegisterForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])

class CourseAddingForm(FlaskForm):
    course_name = StringField("course name", validators=[DataRequired()])
    instructor = StringField("instructor")
    course_day = StringField("course day", validators=[DataRequired()])
    start_time = TimeField("course start time", validators=[DataRequired()])
    end_time = TimeField("course end time", validators=[DataRequired()])
    study_duration = IntegerField()
    submit1 = SubmitField("submit")

class CourseDeleteForm(FlaskForm):
    course_name = StringField()
    im_sure = RadioField(choices=["i'm sure"])
    submit4 = SubmitField("submit")

class EditProfileForm(FlaskForm):
    username = StringField("username")
    first_name = StringField("first name")
    last_name  = StringField("last name")
    phone_num = StringField("phone number")
    email = StringField("email")
    submit1 = SubmitField("submit")

class ExamAddingForm(FlaskForm):
    course_name = StringField("course name", validators=[DataRequired()])
    exam_name = StringField()
    date = DateField("exam date" , validators=[DataRequired()])
    percent = StringField("percent")
    submit2 = SubmitField("submit")

class ExamDeleteForm(FlaskForm):
    course_name = StringField()
    exam_name = StringField()
    im_sure = RadioField(choices=["i'm sure"])
    submit = SubmitField()

class HomeworkAddingForm(FlaskForm):
    course_name = StringField("course name", validators=[DataRequired()])
    hw_name = StringField()
    deadline = DateField("deadline" , validators=[DataRequired()])
    percent = StringField("percent")
    submit3 = SubmitField("submit")

class HomeworkDeleteForm(FlaskForm):
    course_name = StringField()
    hw_name = StringField()
    im_sure = RadioField(choices=["i'm sure"])
    submit = SubmitField()

class StudyDurationForm(FlaskForm):
    start = SubmitField()
    pause = SubmitField()
    stop = SubmitField()

class OneDayForm(FlaskForm):
    day = SelectField(u'Select day', choices=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
    zero_to_one = RadioField(choices=['study', 'not study'], default='not study')
    one_to_two = RadioField(choices=['study', 'not study'], default='not study' )
    two_to_three  = RadioField(choices=['study', 'not study'], default='not study' )
    three_to_four = RadioField(choices=['study', 'not study'], default='not study' )
    four_to_five = RadioField(choices=['study', 'not study'], default='not study' )
    five_to_six = RadioField(choices=['study', 'not study'], default='not study' )
    six_to_seven = RadioField(choices=['study', 'not study'], default='not study' )
    seven_to_eight = RadioField(choices=['study', 'not study'], default='not study' )
    eight_to_nine = RadioField(choices=['study', 'not study'], default='not study' )
    nine_to_ten = RadioField(choices=['study', 'not study'], default='not study' )
    ten_to_eleven = RadioField(choices=['study', 'not study'], default='not study' )
    eleven_to_twelve= RadioField(choices=['study', 'not study'], default='not study' )
    twelve_to_thirteen = RadioField(choices=['study', 'not study'], default='not study' )
    thirteen_to_fourteen = RadioField(choices=['study', 'not study'], default='not study' )
    fourteen_to_fifteen = RadioField(choices=['study', 'not study'], default='not study' )
    fifteen_to_sixteen = RadioField(choices=['study', 'not study'], default='not study' )
    sixteen_to_seventeen= RadioField(choices=['study', 'not study'], default='not study' )
    seventeen_to_eighteen = RadioField(choices=['study', 'not study'], default='not study' )
    eighteen_to_nineteen = RadioField(choices=['study', 'not study'], default='not study' )
    nineteen_to_twenty = RadioField(choices=['study', 'not study'], default='not study' )
    twenty_to_twentyone = RadioField(choices=['study', 'not study'], default='not study' )
    twentyone_to_twentytwo = RadioField(choices=['study', 'not study'], default='not study' )
    twentytwo_to_twentythree= RadioField(choices=['study', 'not study'], default='not study' )
    twentythree_to_twentyfour= RadioField(choices=['study', 'not study'], default='not study' )
    submit2 = SubmitField("submit")