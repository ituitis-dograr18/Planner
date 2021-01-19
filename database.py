from flask import session, redirect, url_for
import random
from datetime import timedelta, date
import time


def register(form, password, mycursor, mydb):
    sql = "INSERT INTO user (username, pword, email) VALUES (%s, %s, %s)"
    value = (form.username.data, password, form.email.data)
    mycursor.execute(sql, value)        
    mydb.commit()

    session['user_id'] = form.username.data    

def add_course_to_user(form, mycursor, mydb):
        
    sql = "SELECT * FROM course WHERE course_name = %s AND course_day = %s AND start_time = %s AND end_time = %s AND instructor = %s"
    val = (form.course_name.data, form.course_day.data, form.start_time.data, form.end_time.data, form.instructor.data)
    mycursor.execute(sql,val)
    course = mycursor.fetchall()
        
    if len(course) == 0: #course yoksa
        #adding new course
        sql = "INSERT INTO course (course_name, course_day, start_time, end_time, instructor ) VALUES (%s, %s, %s, %s, %s)"
        val = (form.course_name.data, form.course_day.data, form.start_time.data, form.end_time.data, form.instructor.data)
        mycursor.execute(sql, val)
        mydb.commit()

    sql = "SELECT * FROM taken_courses INNER JOIN course ON taken_courses.course_id=course.course_id WHERE username = %s AND course_name = %s AND course_day = %s AND start_time = %s AND end_time = %s AND instructor = %s" 
    val = (session['user_id'], form.course_name.data, form.course_day.data, form.start_time.data, form.end_time.data, form.instructor.data)
    mycursor.execute(sql, val)
    match = mycursor.fetchall()
    
    if len(match) == 0: 
        #adding new course for user
        sql = "SELECT * FROM course WHERE course_name = %s AND course_day = %s AND start_time = %s AND end_time = %s AND instructor = %s"
        val = (form.course_name.data, form.course_day.data, form.start_time.data, form.end_time.data, form.instructor.data)
        mycursor.execute(sql, val)
        the_course = mycursor.fetchone()

        sql = "INSERT INTO taken_courses (username, course_id, study_duration) VALUES (%s, %s, %s)"
        val = (session['user_id'], the_course['course_id'], form.study_duration.data)
        mycursor.execute(sql,val)
        mydb.commit()

def add_days_to_user(mycursor, mydb):
    main_sql = """INSERT INTO one_day (day_name,zero_to_one, one_to_two, two_to_three, three_to_four, four_to_five, five_to_six, 
        six_to_seven, seven_to_eight, eight_to_nine, nine_to_ten, ten_to_eleven, eleven_to_twelve, twelve_to_thirteen, 
        thirteen_to_fourteen, fourteen_to_fifteen, fifteen_to_sixteen, sixteen_to_seventeen, seventeen_to_eighteen, 
        eighteen_to_nineteen, nineteen_to_twenty, twenty_to_twenty, twentyone_to_twentytwo, twentytwo_to_twentythree, 
        twentythreee_to_twentyfour) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    #monday
    val = ("monday", 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study',)
    mycursor.execute(main_sql, val)
    mydb.commit()

    sql = "SELECT * FROM one_day ORDER BY day_id DESC LIMIT 1"
    mycursor.execute(sql)
    the_day = mycursor.fetchone()
    
    sql = "UPDATE user set monday=%s WHERE username=%s"
    val = (the_day['day_id'], session['user_id'])
    mycursor.execute(sql, val)
    mydb.commit()

    #tuesday
    val = ("tuesday", 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study',)
    mycursor.execute(main_sql, val)
    mydb.commit()

    sql = "SELECT * FROM one_day ORDER BY day_id DESC LIMIT 1"
    mycursor.execute(sql)
    the_day = mycursor.fetchone()

    sql = "UPDATE user set tuesday=%s WHERE username=%s"
    val = (the_day['day_id'], session['user_id'])
    mycursor.execute(sql, val)
    mydb.commit()
    
    #wenesday
    val = ("wednesday", 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study',)
    mycursor.execute(main_sql, val)
    mydb.commit()

    sql = "SELECT * FROM one_day ORDER BY day_id DESC LIMIT 1"
    mycursor.execute(sql)
    the_day = mycursor.fetchone()


    sql = "UPDATE user set wednesday=%s WHERE username=%s"
    val = (the_day['day_id'], session['user_id'])
    mycursor.execute(sql, val)
    mydb.commit()
    
    #thursday
    val = ("thursday", 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study',)
    mycursor.execute(main_sql, val)
    mydb.commit()

    sql = "SELECT * FROM one_day ORDER BY day_id DESC LIMIT 1"
    mycursor.execute(sql)
    the_day = mycursor.fetchone()

    sql = "UPDATE user set thursday=%s WHERE username=%s"
    val = (the_day['day_id'], session['user_id'])
    mycursor.execute(sql, val)
    mydb.commit()
    
    #friday
    val = ("friday", 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study',)
    mycursor.execute(main_sql, val)
    mydb.commit()

    sql = "SELECT * FROM one_day ORDER BY day_id DESC LIMIT 1"
    mycursor.execute(sql)
    the_day = mycursor.fetchone()

    sql = "UPDATE user set friday=%s WHERE username=%s"
    val = (the_day['day_id'], session['user_id'])
    mycursor.execute(sql, val)
    mydb.commit()
    
    #saturday
    val = ("saturday", 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study',)
    mycursor.execute(main_sql, val)
    mydb.commit()

    sql = "SELECT * FROM one_day ORDER BY day_id DESC LIMIT 1"
    mycursor.execute(sql)
    the_day = mycursor.fetchone()

    sql = "UPDATE user set saturday=%s WHERE username=%s"
    val = (the_day['day_id'], session['user_id'])
    mycursor.execute(sql, val)
    mydb.commit()
    
    #sunday
    val = ("sunday", 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study', 'not study',)
    mycursor.execute(main_sql, val)
    mydb.commit()

    sql = "SELECT * FROM one_day ORDER BY day_id DESC LIMIT 1"
    mycursor.execute(sql)
    the_day = mycursor.fetchone()

    sql = "UPDATE user set sunday=%s WHERE username=%s"
    val = (the_day['day_id'], session['user_id'])
    mycursor.execute(sql, val)
    mydb.commit()

def add_exam(form, mycursor, mydb):
    #find the course
    sql = "SELECT * FROM taken_courses INNER JOIN course ON taken_courses.course_id=course.course_id WHERE (username = %s AND course_name = %s)"
    val = (session['user_id'], form.course_name.data)
    mycursor.execute(sql, val)
    the_course = mycursor.fetchone()

    #add exam
    sql = "INSERT INTO exam (username, course_id, exam_date, percent, exam_name) VALUES(%s, %s, %s, %s, %s)"
    val = (session['user_id'], the_course['course_id'], form.date.data, form.percent.data, form.exam_name.data)
    mycursor.execute(sql, val)
    mydb.commit()

def add_hw(form, mycursor, mydb):

    #find course
    sql = "SELECT * FROM taken_courses INNER JOIN course ON taken_courses.course_id=course.course_id WHERE (username =%s AND course_name=%s)"
    val = (session['user_id'], form.course_name.data)
    mycursor.execute(sql, val)
    the_course = mycursor.fetchone()

    #add hw
    sql = "INSERT INTO homework (username, course_id, deadline, percent, hw_name) VALUES(%s, %s, %s, %s, %s)"
    val = (session['user_id'], the_course['course_id'], form.deadline.data, form.percent.data, form.hw_name.data)
    mycursor.execute(sql, val)
    mydb.commit()

def check_day(day, mycursor, mydb):
    var = []

    for x in day.keys():
        if x != 'day_id' and x != 'day_name':
            if day[x]== None or day[x] == '0':
                day[x] = 'not study'
                var.append(day[x])
            else:
                var.append(day[x])
    var.append(day['day_id'])
    t = tuple(var)
    
    sql = """UPDATE one_day SET zero_to_one=%s, one_to_two=%s, two_to_three=%s, three_to_four=%s, four_to_five=%s, five_to_six=%s, 
        six_to_seven=%s, seven_to_eight=%s, eight_to_nine=%s, nine_to_ten=%s, ten_to_eleven=%s, eleven_to_twelve=%s, twelve_to_thirteen=%s, 
        thirteen_to_fourteen=%s, fourteen_to_fifteen=%s, fifteen_to_sixteen=%s, sixteen_to_seventeen=%s, seventeen_to_eighteen=%s, 
        eighteen_to_nineteen=%s, nineteen_to_twenty=%s, twenty_to_twenty=%s, twentyone_to_twentytwo=%s, twentytwo_to_twentythree=%s, 
        twentythreee_to_twentyfour=%s WHERE day_id=%s
        """    
    mycursor.execute(sql, t)
    mydb.commit()

def check_times(mycursor, mydb):
    #her gün için data bul
    sql = "SELECT * FROM user WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    user = mycursor.fetchone()

    # tek tek kontrol et 
    sql = "SELECT * FROM one_day WHERE day_id = %s"
    mycursor.execute(sql, (user['monday'], ))
    day = mycursor.fetchone()
    check_day(day, mycursor, mydb)

    mycursor.execute(sql, (user['tuesday'], ))
    day = mycursor.fetchone()
    check_day(day, mycursor, mydb)

    mycursor.execute(sql, (user['wednesday'], ))
    day = mycursor.fetchone()
    check_day(day, mycursor, mydb)

    mycursor.execute(sql, (user['thursday'], ))
    day = mycursor.fetchone()
    check_day(day, mycursor, mydb)

    mycursor.execute(sql, (user['friday'], ))
    day = mycursor.fetchone()
    check_day(day, mycursor, mydb)

    mycursor.execute(sql, (user['saturday'], ))
    day = mycursor.fetchone()
    check_day(day, mycursor, mydb)

    mycursor.execute(sql, (user['sunday'], ))
    day = mycursor.fetchone()
    check_day(day, mycursor, mydb)

def create_events(exams, hws):
    week1 = {}
    week2 = {}
    week3 = {}
    week4 = {}
    today = date.today()
    day_names = []

    for i in range(0,7):
        day_names.append(today.strftime("%A"))
        today += timedelta(days=1)
    
    today = date.today()
    print()

    #for week1
    for x in range(0, 7):
        week1[str(today)] = ""
        for exam in exams:
            if exam['exam_date'] == today:
                add = exam['course_name'] + " Exam"
                week1[str(today)] = add
            
        for hw in hws:
            if hw['deadline'] == today:
                add = hw['course_name'] + " " + hw['hw_name']
                week1[str(today)] = week1[str(today)] + add

        today += timedelta(days=1)

    #for week2
    for x in range(0, 7):
        week2[str(today)] = ""
        for exam in exams:
            if exam['exam_date'] == today:
                add = exam['course_name'] + " Exam"
                week2[str(today)] = add
            
        for hw in hws:
            if hw['deadline'] == today:
                add = hw['course_name'] + " " + hw['hw_name']
                week2[str(today)] = week2[str(today)] + add

        today += timedelta(days=1)

    #for week3
    for x in range(0, 7):
        week3[str(today)] = ""

        for exam in exams:
            if exam['exam_date'] == today:
                add = exam['course_name'] + " Exam"
                week3[str(today)] = add
            
        for hw in hws:
            if hw['deadline'] == today:
                add = hw['course_name'] + " " + hw['hw_name']
                week3[str(today)] = week3[str(today)] + add

        today += timedelta(days=1)
    
    #for week4
    for x in range(0, 7):
        week4[str(today)] = ""

        for exam in exams:
            if exam['exam_date'] == today:
                add = exam['course_name'] + " Exam"
                week4[str(today)] = add
            
        for hw in hws:
            if hw['deadline'] == today:
                add = hw['course_name'] + " " + hw['hw_name']
                week4[str(today)] = week4[str(today)] + add

        today += timedelta(days=1)


    list1 = []
    for x,y in week1.items():
        add = str(x) + " : " + y
        list1.append(add)

    list2 = []
    for x,y in week2.items():
        add = str(x) + " : " + y
        list2.append(add)

    list3 = []
    for x,y in week3.items():
        add = str(x) + " : " + y
        list3.append(add)

    list4 = []
    for x,y in week4.items():
        add = str(x) + " : " + y
        list4.append(add)


    return (day_names, list1, list2, list3, list4)

def create_schedule(mycursor):
    #create list for çalışılacak dersler her dersi listeye study duration kadar ekle
    sql = "SELECT * FROM taken_courses INNER JOIN course ON taken_courses.course_id=course.course_id WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    courses = mycursor.fetchall()

    #dersler, çalışılacak saat dictionary
    study_courses = {}
    study_hours = 0
    for course in courses:
        study_courses[course['course_name']] = course['study_duration']
        study_hours += course['study_duration']
    
    #ders çalışılacak zamanları tutan list
    study_times = []
    available_hours = 0
    #for mondays
    sql = "SELECT * FROM one_day INNER JOIN user ON one_day.day_id=user.monday WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    monday = mycursor.fetchone()

    for hour,avab in monday.items():
        if avab == "study":
            study_times.append(["monday", hour])
            available_hours += 1
    
    #for tuesday
    sql = "SELECT * FROM one_day INNER JOIN user ON one_day.day_id=user.tuesday WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    tuesday = mycursor.fetchone()

    for hour,avab in tuesday.items():
        if avab == "study":
            study_times.append(["tuesday", hour])
            available_hours += 1


    #for wednesday
    sql = "SELECT * FROM one_day INNER JOIN user ON one_day.day_id=user.wednesday WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    wednesday = mycursor.fetchone()

    for hour,avab in wednesday.items():
        if avab == "study":
            study_times.append(["wednesday", hour])
            available_hours += 1


    #for thursday
    sql = "SELECT * FROM one_day INNER JOIN user ON one_day.day_id=user.thursday WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    thursday = mycursor.fetchone()

    for hour,avab in thursday.items():
        if avab == "study":
            study_times.append(["thursday", hour])
            available_hours += 1


    #for friday
    sql = "SELECT * FROM one_day INNER JOIN user ON one_day.day_id=user.friday WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    friday = mycursor.fetchone()

    for hour,avab in friday.items():
        if avab == "study":
            study_times.append(["friday", hour])
            available_hours += 1


    #for saturday
    sql = "SELECT * FROM one_day INNER JOIN user ON one_day.day_id=user.saturday WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    saturday = mycursor.fetchone()

    for hour,avab in saturday.items():
        if avab == "study":
            study_times.append(["saturday", hour])
            available_hours += 1

    #for sunday
    sql = "SELECT * FROM one_day INNER JOIN user ON one_day.day_id=user.sunday WHERE username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    sunday = mycursor.fetchone()

    for hour,avab in sunday.items():
        if avab == "study":
            study_times.append(["sunday", hour])
            available_hours += 1


    #list = [(day, hour, course), ...]
    
    total = []
    i = 0

    if study_hours > available_hours:
        return total 

    for m,n in study_courses.items():
        for dur in range(0,n):
            day = study_times[i][0]
            hour = study_times[i][1]
            total.append([day, hour, m+" study"])
            i += 1

    return total

def create_totalnew(total):
    totalnew = total
    for x in totalnew:
        if x[1] == "zero_to_one":
            x[1] = "00:00 - 01:00"

        elif x[1] == "one_to_two":
            x[1] = "01:00 - 02:00"
        
        elif x[1] == "two_to_three":
            x[1] = "02:00 - 03:00"
            
        elif x[1] == "three_to_four":
            x[1] = "03:00 - 04:00"
        
        elif x[1] == "four_to_five":
            x[1] = "04:00 - 05:00"
        
        elif x[1] == "five_to_six":
            x[1] = "05:00 - 06:00"
        
        elif x[1] == "six_to_seven":
            x[1] = "06:00 - 07:00"
        
        elif x[1] == "seven_to_eight":
            x[1] = "07:00 - 08:00"
        
        elif x[1] == "eight_to_nine":
            x[1] = "08:00 - 09:00"
        
        elif x[1] == "nine_to_ten":
            x[1] = "09:00 - 10:00"
        
        elif x[1] == "ten_to_eleven":
            x[1] = "10:00 - 11:00"
        
        elif x[1] == "eleven_to_twelve":
            x[1] = "11:00 - 12:00"
        
        elif x[1] == "twelve_to_thirteen":
            x[1] = "12:00 - 13:00"
        
        elif x[1] == "thirteen_to_fourteen":
            x[1] = "13:00 - 14:00"
        
        elif x[1] == "fourteen_to_fifteen":
            x[1] = "14:00 - 15:00"
        
        elif x[1] == "fifteen_to_sixteen":
            x[1] = "15:00 - 16:00"
        
        elif x[1] == "sixteen_to_seventeen":
            x[1] = "16:00 - 17:00"
        
        elif x[1] == "seventeen_to_eighteen":
            x[1] = "17:00 - 18:00"
        
        elif x[1] == "eighteen_to_nineteen":
            x[1] = "18:00 - 19:00"
        
        elif x[1] == "nineteen_to_twenty":
            x[1] = "19:00 - 20:00"
        
        elif x[1] == "twenty_to_twentyone":
            x[1] = "20:00 - 21:00"
        
        elif x[1] == "twentyone_to_twentytwo":
            x[1] = "21:00 - 22:00"
        
        elif x[1] == "twentytwo_to_twentythree":
            x[1] = "22:00 - 23:00"
        
        elif x[1] == "twentythree_to_twentyfour":
            x[1] = "23:00 - 24:00"
        
    return totalnew

def what_time(total):

    clock = time.localtime()
    day = date.today()
    day = day.strftime("%A")
    day = day.lower()


    time_for = ""

    for x in total:
        if day == x[0]:
            if x[1] == "zero_to_one" and clock.tm_hour < 1 :
                time_for = x[2]

            elif x[1] == "one_to_two" and clock.tm_hour < 2:
                time_for = x[2]
            
            elif x[1] == "two_to_three" and clock.tm_hour < 3:
                time_for = x[2]
                
            elif x[1] == "three_to_four" and clock.tm_hour < 4:
                time_for = x[2]
            
            elif x[1] == "four_to_five" and clock.tm_hour < 5:
                time_for = x[2]
                
            elif x[1] == "five_to_six" and clock.tm_hour < 6:
                time_for = x[2]
            
            elif x[1] == "six_to_seven" and clock.tm_hour < 7:
                time_for = x[2]
            
            elif x[1] == "seven_to_eight" and clock.tm_hour < 8:
                time_for = x[2]
            
            elif x[1] == "eight_to_nine" and clock.tm_hour < 9:
                time_for = x[2]
            
            elif x[1] == "nine_to_ten" and clock.tm_hour < 10:
                time_for = x[2]
            
            elif x[1] == "ten_to_eleven" and clock.tm_hour < 11:
                time_for = x[2]
            
            elif x[1] == "eleven_to_twelve" and clock.tm_hour < 12:
                time_for = x[2]
            
            elif x[1] == "twelve_to_thirteen" and clock.tm_hour < 13:
                time_for = x[2]
            
            elif x[1] == "thirteen_to_fourteen" and clock.tm_hour < 14:
                time_for = x[2]

            elif x[1] == "fourteen_to_fifteen" and clock.tm_hour < 15:
                time_for = x[2]
            
            elif x[1] == "fifteen_to_sixteen" and clock.tm_hour < 16:
                time_for = x[2]
            
            elif x[1] == "sixteen_to_seventeen" and clock.tm_hour < 17:
                time_for = x[2]
            
            elif x[1] == "seventeen_to_eighteen" and clock.tm_hour < 18:
                time_for = x[2]
            
            elif x[1] == "eighteen_to_nineteen" and clock.tm_hour < 19:
                time_for = x[2]
            
            elif x[1] == "nineteen_to_twenty" and clock.tm_hour < 20:
                time_for = x[2]
            
            elif x[1] == "twenty_to_twentyone" and clock.tm_hour < 21:
                time_for = x[2]
            
            elif x[1] == "twentyone_to_twentytwo" and clock.tm_hour < 22:
                time_for = x[2]
            
            elif x[1] == "twentytwo_to_twentythree" and clock.tm_hour < 23:
                time_for = x[2]
            
            elif x[1] == "twentythree_to_twentyfour" and clock.tm_hour < 24:
                time_for = x[2]
    
    
    if time_for == "":
        time_for = "empty"
    else:
        time_for += " studying"

    return time_for

def course_delete(form, mycursor, mydb):
    if form.im_sure.data == None:
        return redirect(url_for('edit_courses_page'))
    
    sql = "SELECT * FROM taken_courses INNER JOIN course ON taken_courses.course_id=course.course_id WHERE username=%s AND course_name=%s"
    mycursor.execute(sql, (session['user_id'], form.course_name.data))
    course = mycursor.fetchone()

    id = course['course_id']

    sql = "SELECT * FROM course WHERE course_id=%s"
    mycursor.execute(sql, (id, ))
    courses = mycursor.fetchall()

    if len(courses) > 1:
        #dersi alan birden fazla kişi var sadece takencoursedan sil
        sql = "DELETE FROM taken_courses WHERE username=%s AND course_id=%s"
        mycursor.execute(sql, (session['user_id'], id))

    else:
        sql = "DELETE FROM course WHERE course_id=%s"
        mycursor.execute(sql, (id, ))

    mydb.commit()

def exam_delete(mycursor, mydb, exs):
    for e in exs:
        sql = "delete from exam where exam_id=%s"
        mycursor.execute(sql, (e, ))
        mydb.commit()

def homework_delete(mycursor, mydb, hws):
    for h in hws:
        sql = "delete from homework where homework_id=%s"
        mycursor.execute(sql, (h, ))
        mydb.commit()
    
def update_day(day_form, mycursor,mydb):
    
    sql = "SELECT * FROM user WHERE username = %s"
    mycursor.execute(sql, (session['user_id'], ))
    user = mycursor.fetchone()
    
    sql = """UPDATE one_day SET zero_to_one=%s, one_to_two=%s, two_to_three=%s, three_to_four=%s, four_to_five=%s, five_to_six=%s, 
    six_to_seven=%s, seven_to_eight=%s, eight_to_nine=%s, nine_to_ten=%s, ten_to_eleven=%s, eleven_to_twelve=%s, twelve_to_thirteen=%s, 
    thirteen_to_fourteen=%s, fourteen_to_fifteen=%s, fifteen_to_sixteen=%s, sixteen_to_seventeen=%s, seventeen_to_eighteen=%s, 
    eighteen_to_nineteen=%s, nineteen_to_twenty=%s, twenty_to_twenty=%s, twentyone_to_twentytwo=%s, twentytwo_to_twentythree=%s, 
    twentythreee_to_twentyfour=%s WHERE day_id=%s
    """
    val = (day_form.zero_to_one.data, day_form.one_to_two.data, day_form.two_to_three.data, day_form.three_to_four.data, day_form.four_to_five.data,
    day_form.five_to_six.data, day_form.six_to_seven.data, day_form.seven_to_eight.data, day_form.eight_to_nine.data, day_form.nine_to_ten.data, 
    day_form.ten_to_eleven.data, day_form.eleven_to_twelve.data, day_form.twelve_to_thirteen.data, day_form.thirteen_to_fourteen.data, 
    day_form.fourteen_to_fifteen.data, day_form.fifteen_to_sixteen.data, day_form.sixteen_to_seventeen.data, day_form.seventeen_to_eighteen.data, 
    day_form.eighteen_to_nineteen.data, day_form.nineteen_to_twenty.data, day_form.twenty_to_twentyone.data, day_form.twentyone_to_twentytwo.data, 
    day_form.twentytwo_to_twentythree.data, day_form.twentythree_to_twentyfour.data, user[day_form.day.data])
    mycursor.execute(sql, val)
    mydb.commit()

def update_profile(form, mycursor,mydb):
    sql = "UPDATE user SET first_name = %s, last_name = %s, email =%s ,phone =%s WHERE username = %s"
    val = (form.first_name.data, form.last_name.data, form.email.data, form.phone_num.data, session['user_id'])
    mycursor.execute(sql, val)
    mydb.commit()

def delete_account(mycursor, mydb):
    sql = "select * from user where username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    user = mycursor.fetchone()

    days = [user['monday'], user['tuesday'], user['wednesday'], user['thursday'], user['friday'], user['saturday'], user['sunday'], ]

    for day in days:
        sql = "delete from one_day where day_id=%s"
        val = (day, )
        mycursor.execute(sql, val)
        mydb.commit()

def course_schedule(mycursor):
    #[day, 11:00 - 12:00, ders adı]

    sql = "select * from course inner join taken_courses on taken_courses.course_id=course.course_id where username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    courses = mycursor.fetchall()

    total = []
    for course in courses:
        c = []
        start = str(course['start_time']).split(":")
        start = start[0]
        start = int(start)
        end = str(course['end_time']).split(":")
        end = end[0]
        end= int(end)
        
        for x in range(start,end):
            y = str(x)
            z = str(x+1)
            if len(y) == 1:
                y = "0" + y
            if len(z) == 1:
                z = "0" + z
            
            add = y + ":00 - " + z + ":00"
            c = [course['course_day'], add, course["course_name"]]
            total.append(c)
            c = []

    return total            

def finish_hws(completed, mycursor, mydb):
    for x in completed:
       sql = "update homework set hw_status='1' where homework_id=%s"
       mycursor.execute(sql, (x, ))
       mydb.commit()

def group(mycursor):
    sql = "select * from taken_courses inner join course on taken_courses.course_id=course.course_id where username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    courses = mycursor.fetchall()

    sql = "select course_id, count(*) from taken_courses group by course_id"
    mycursor.execute(sql)
    grouped = mycursor.fetchall()

    r = []

    for x in courses:
        for y in grouped:
            if x['course_id'] == y['course_id']:
                r.append([x['course_name'], y['count(*)']])

    return r

def average_study_duration(mycursor):
    sql = "select * from taken_courses inner join course on taken_courses.course_id=course.course_id where username=%s"
    mycursor.execute(sql, (session['user_id'], ))
    courses = mycursor.fetchall()
    
    sql = "select course_id, avg(study_duration) from taken_courses group by course_id"
    mycursor.execute(sql)
    grouped = mycursor.fetchall()

    r = []

    for x in courses:
        for y in grouped:
            if x['course_id'] == y['course_id']:
                r.append([x['course_name'], round(y['avg(study_duration)'], 2) ])


    return r









