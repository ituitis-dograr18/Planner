struct = []

sql = """create table if not exists one_day(
    day_id int auto_increment,
    zero_to_one varchar(15) default 'not study',
    one_to_two varchar(15) default 'not study',
    two_to_three varchar(10) default 'not study',
    three_to_four varchar(10) default 'not study',
    four_to_five varchar(10) default 'not study',
    five_to_six varchar(10) default 'not study',
    six_to_seven varchar(10) default 'not study',
    seven_to_eight varchar(10) default 'not study',
    eight_to_nine varchar(10) default 'not study',
    nine_to_ten varchar(10) default 'not study',
    ten_to_eleven varchar(10) default 'not study',
    eleven_to_twelve varchar(10) default 'not study',
    twelve_to_thirteen varchar(10) default 'not study',
    thirteen_to_fourteen varchar(10) default 'not study',
    fourteen_to_fifteen varchar(10) default 'not study',
    fifteen_to_sixteen varchar(10) default 'not study',
    sixteen_to_seventeen varchar(10) default 'not study',
    seventeen_to_eighteen varchar(10) default 'not study',
    eighteen_to_nineteen varchar(10) default 'not study',
    nineteen_to_twenty varchar(10) default 'not study',
    twenty_to_twenty varchar(10) default 'not study',
    twentyone_to_twentytwo varchar(10) default 'not study',
    twentytwo_to_twentythree varchar(10) default 'not study',
    twentythreee_to_twentyfour varchar(10) default 'not study',
    day_name varchar(10) not null,
    primary key(day_id)
)
"""
struct.append(sql)

sql = """create table if not exists user(
    username varchar(20),
    pword varchar(100) not null,
    first_name varchar(20) default "",
    last_name varchar(20) default "",
    email varchar(30) not null,
    phone varchar(15) default "",
    score int default 0,
    monday int,
    tuesday int,
    wednesday int,
    thursday int,
    friday int,
    saturday int,
    sunday int,
    primary key(username),
    foreign key(monday) references one_day(day_id) on delete cascade,
    foreign key(tuesday) references one_day(day_id) on delete cascade,
    foreign key(wednesday) references one_day(day_id) on delete cascade, 
    foreign key(thursday) references one_day(day_id) on delete cascade, 
    foreign key(friday) references one_day(day_id) on delete cascade,
    foreign key(saturday) references one_day(day_id) on delete cascade, 
    foreign key(sunday) references one_day(day_id) on delete cascade
    )
"""
struct.append(sql)

sql = """create table if not exists course(
    course_id int auto_increment,
    course_name varchar(30),
    instructor varchar(30),
    course_day varchar(10),
    start_time time,
    end_time time,
    primary key(course_id)
    )
"""
struct.append(sql)

sql = """create table if not exists taken_courses(
    enrollment_id int auto_increment,
    username varchar(20),
    course_id int,
    study_duration int,
    studied_time int,
    primary key(enrollment_id),
    foreign key(username) references user(username) on delete cascade,
    foreign key(course_id) references course(course_id) on delete cascade
)
"""
struct.append(sql)

sql = """create table if not exists exam(
    exam_id int auto_increment,
    exam_name varchar(45) not null,
    username varchar(20),
    course_id int,
    percent int,
    exam_date date,
    primary key(exam_id),
    foreign key(username) references user(username) on delete cascade,
    foreign key(course_id) references course(course_id) on delete cascade
)
"""
struct.append(sql)

sql = """create table if not exists homework(
    homework_id int auto_increment,
    hw_name varchar(40) not null,
    username varchar(20),
    course_id int,
    percent int,
    spent_time int default 0,
    deadline date,
    hw_status boolean default false,
    primary key(homework_id),
    foreign key(username) references user(username) on delete cascade,
    foreign key(course_id) references course(course_id) on delete cascade
)
"""
struct.append(sql)
