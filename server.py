from flask import Flask, render_template, request, session, redirect, url_for
from flask_login import LoginManager
from forms import LoginForm, RegisterForm, EditProfileForm, CourseAddingForm, OneDayForm, ExamAddingForm, HomeworkAddingForm, StudyDurationForm, CourseDeleteForm
from forms import HomeworkDeleteForm, ExamDeleteForm, DeleteMeForm
import mysql.connector
from database import add_hw, add_exam, add_days_to_user, add_course_to_user, check_times, create_events, create_schedule
from database import course_delete, create_totalnew, what_time, exam_delete, homework_delete, register, update_day, update_profile
from database import delete_account, course_schedule, finish_hws, group, average_study_duration
from datetime import datetime, timedelta, date
import random 
from passlib.hash import pbkdf2_sha256 as hasher
import structs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecretkey'


mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="planner")
mycursor = mydb.cursor(dictionary=True)

for s in structs.struct:
    mycursor.execute(s)
    mydb.commit()

@app.route('/')
def home_page():
    i = random.randint(1,5)
    bg = "background" + str(i) +".jpg" 
    return render_template("home.html", bg=bg)

@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile_page(username):
    if 'user_id' not in session :
        return redirect('/')

    grouped = group(mycursor)
    r = average_study_duration(mycursor)

    #for exams
    sql = "SELECT * FROM exam INNER JOIN course ON exam.course_id=course.course_id WHERE username = %s"
    val = (username, )
    mycursor.execute(sql, val)
    exams = mycursor.fetchall()

    #for homeworks
    sql = "SELECT * FROM homework INNER JOIN course ON homework.course_id=course.course_id WHERE username = %s"
    val = (username, )
    mycursor.execute(sql, val)
    homeworks = mycursor.fetchall()

    total = create_schedule(mycursor)
    time_for = what_time(total)

    return render_template("profile.html", name=username, exams=exams, homeworks=homeworks, time_for=time_for, grouped=grouped, r=r)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():

        sql = "select pword from user where username=%s"
        mycursor.execute(sql, (form.username.data, ))
        pw = mycursor.fetchone()
        pw = pw['pword']

        verify = hasher.verify(form.password.data, pw)

        if verify == True:
            session['user_id'] = form.username.data
            return redirect(url_for('profile_page', username=session['user_id']))
  
    return render_template("login.html", form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile_page():
    if 'user_id' not in session :
        return redirect('/')

    edit_form = EditProfileForm(request.form)
    day_form = OneDayForm(request.form)
    deleteme = DeleteMeForm(request.form)

    sql = "SELECT * FROM user WHERE username = %s"
    mycursor.execute(sql, (session['user_id'], ))
    user = mycursor.fetchone()

    if edit_form.validate_on_submit() and edit_form.submit1.data == True:
        update_profile(edit_form, mycursor, mydb)
        return redirect(url_for('edit_profile_page'))
        
    if deleteme.validate_on_submit() and deleteme.submit3.data == True:
        if deleteme.delacc.data == "Delete Account":
            delete_account(mycursor, mydb)
            session.pop('user_id')
            return redirect(url_for('home_page'))

        else:
            return redirect(url_for('edit_profile_page'))


    if day_form.submit2.data == True:
        update_day(day_form, mycursor, mydb)

        check_times(mycursor, mydb)
        return redirect(url_for('edit_profile_page'))

    

    return render_template("edit_profile.html", edit_form=edit_form, day_form=day_form, user=user, deleteme=deleteme)

@app.route('/exams', methods=['GET', 'POST'])
def exams_page():
    if 'user_id' not in session :
        return redirect('/')

    username = session['user_id']
    today = date.today()

    if request.method == 'POST':
        exs = request.form.getlist('deletebox')
        exam_delete(mycursor, mydb, exs)
        return redirect(url_for('exams_page'))

    sql = "SELECT * FROM exam INNER JOIN course ON exam.course_id=course.course_id WHERE username = %s"
    val = (username, )
    mycursor.execute(sql, val)
    exams = mycursor.fetchall()
    
    past = 0
    future = 0
    for e in exams:
        if e['exam_date'] < today:
            past += 1
        else:
            future += 1

    return render_template("exams.html", exams=exams, today=today, past=past, future=future)

@app.route('/homeworks', methods=['GET', 'POST'])
def homeworks_page():
    if 'user_id' not in session :
        return redirect('/')

    today = date.today()

    if request.method == 'POST':
        hw = request.form.getlist('deletebox')
        homework_delete(mycursor, mydb, hw)

        completed = request.form.getlist('succesbox')
        finish_hws(completed, mycursor, mydb)

        return redirect(url_for('homeworks_page'))

    sql = "SELECT * FROM homework INNER JOIN course ON homework.course_id=course.course_id WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    homeworks = mycursor.fetchall()

    

    past = 0
    future = 0

    for h in homeworks:
        if h['deadline'] < today:
            past += 1
        else:
            future += 1

    return render_template("homeworks.html", homeworks=homeworks, past=past, future=future, today=today)

@app.route('/edit_courses', methods=['GET', 'POST'])
def edit_courses_page():
    if 'user_id' not in session :
        return redirect('/')
    
    course_form = CourseAddingForm(request.form)
    exam_form = ExamAddingForm(request.form)
    hw_form = HomeworkAddingForm(request.form)
    course_del_form = CourseDeleteForm(request.form)

    if course_form.validate_on_submit() and course_form.submit1.data == True:
        print("a")
        add_course_to_user(course_form, mycursor, mydb)
        return redirect(url_for('edit_courses_page'))

    if exam_form.is_submitted() and exam_form.submit2.data == True:
        print("b")
        add_exam(exam_form, mycursor, mydb)
        return redirect(url_for('edit_courses_page'))

    if hw_form.is_submitted() and hw_form.submit3.data == True:
        print("c")
        add_hw(hw_form, mycursor, mydb)
        return redirect(url_for('edit_courses_page'))

    if course_del_form.validate_on_submit() and course_del_form.submit4.data == True:
        course_delete(course_del_form, mycursor, mydb)
        return redirect(url_for('edit_courses_page'))

    return render_template("edit_courses.html", course_form=course_form, exam_form=exam_form, hw_form=hw_form, course_del_form=course_del_form)

@app.route('/ajanda')
def ajanda_page():
    if 'user_id' not in session :
        return redirect('/')
    
    sql = "SELECT * FROM exam INNER JOIN course ON exam.course_id=course.course_id WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    exams = mycursor.fetchall()

    sql = "SELECT * FROM homework INNER JOIN course ON homework.course_id=course.course_id WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    hws = mycursor.fetchall()

    day_names, week1, week2, week3, week4 = create_events(exams, hws)

    return render_template("ajanda.html", day_names=day_names, week1=week1, week2=week2, week3=week3, week4=week4)

@app.route('/schedule')
def schedule_page():
    if 'user_id' not in session :
        return redirect('/')
    
    total = create_schedule(mycursor)
    courses = course_schedule(mycursor)
    totalnew = create_totalnew(total)
    
    add = True
    for i in courses:
        for j in totalnew:
            if i[0] == j[0] and i[1] == j[1]:
                add = False

        if add == True:
            totalnew.append(i)
        add = True

    totalnew.sort()

    return render_template("schedule.html", total=totalnew)

@app.route('/register',methods=['GET', 'POST'])
def signup_page():
    form = RegisterForm(request.form)
    
    if form.validate_on_submit():
        print("in")
        sql = "SELECT * FROM user WHERE username = %s"
        mycursor.execute(sql, (form.username.data, ))
        same_username = mycursor.fetchall()

        if len(same_username) > 0:
            return render_template("register.html", form=form)

        hashed = hasher.hash(form.password.data)
        register(form, hashed, mycursor, mydb)
        add_days_to_user(mycursor, mydb)

        return redirect(url_for('profile_page', username=session['user_id']))
    
    else:
        return render_template("register.html", form=form)

@app.route('/logout')
def logout_page():
    if 'user_id' not in session :
        return redirect('/')

    session.pop('user_id')
    return redirect('/')


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080, debug=True)
    