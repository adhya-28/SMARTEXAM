import pymysql
#import MySQLdb


def connection():
    #conn = MySQLdb.connect(db='exam', user='root', passwd='root', host='localhost')
    conn = pymysql.connect(host="localhost", user="root",password="root", db="exam")
    #conn = pymysql.connect(host="127.0.0.1", user="root",password="root", db="exam")
    c = conn.cursor()
    return c, conn


def check_login(username, password):
    print("login function")
    c, conn = connection()
    query_string = "select * from tbl_login where username='" + \
        username+"' and password='"+password+"' and status='Verified'"
    print(query_string)
    c.execute(query_string)
    data = c.fetchall()
    if len(data) == 1:
        return (["true", data[0][0], data[0][1], data[0][3]])
        print("success")
    else:
        return (["false"])


def add_questions(subjectid, question, answer, keyans, weight, date):
    c, conn = connection()
    sql = "INSERT INTO tbl_addquestions (subject_id, question, answer, answer_key, weight_of_question,  date) VALUES (" + \
        subjectid+",'"+question+"','"+answer+"', '"+keyans+"', "+weight+", '"+date+"')"
    c.execute(sql)
    print("inserted successfully")
    conn.commit()
    return 'OK'


def addsem(course, sem):
    c, conn = connection()
    c.execute("select * from tbl_semester where cousre_id='" +
              course+"' and semester='"+sem+"'")
    if (c.rowcount == 0):
        sql = "INSERT INTO tbl_semester (cousre_id,semester) VALUES ('" + \
            course+"','"+sem+"')"
        c.execute(sql)
        print("inserted successfully")
        conn.commit()
        return 'OK'
    else:
        return 'semester already exists'


def addsub(course, sem, sub):
    c, conn = connection()
    c.execute("select * from tbl_subject where semester_id='" +
              sem+"' and subject='"+sub+"'")
    if (c.rowcount == 0):
        sql = "INSERT INTO tbl_subject (semester_id,subject) VALUES ('" + \
            sem+"','"+sub+"')"
        c.execute(sql)
        print("inserted successfully")
        conn.commit()
        return 'OK'
    else:
        return 'subject already exists'


def addweight(course, sem, sub, weight):
    c, conn = connection()
    c.execute("select * from tbl_weight where subject_id='" +
              sub+"' and weight='"+weight+"'")
    if (c.rowcount == 0):
        sql = "INSERT INTO tbl_weight (subject_id,weight) VALUES ('" + \
            sub+"','"+weight+"')"
        c.execute(sql)
        print("inserted successfully")
        conn.commit()
        return 'OK'
    else:
        return 'weightage already exists'


def qpset(course, sem, sub, weight, no):
    c, conn = connection()
    c.execute("select * from tbl_qpweight where subject_id='" +
              sub+"' and weight='"+weight+"'")
    if (c.rowcount == 0):
        sql = "INSERT INTO tbl_qpweight (subject_id,weight,no) VALUES ('" + \
            sub+"','"+weight+"','"+no+"')"
        c.execute(sql)
        print("inserted successfully")
        conn.commit()
        return 'OK'
    else:
        return 'weightage already exists'


def addcourse(course):
    c, conn = connection()
    #c.execute("select * from tbl_course where cousre='"+course+"'")
    #new
    c.execute("SELECT * FROM tbl_course WHERE course = %s", (course,))
    if (c.rowcount == 0):
        sql = "INSERT INTO tbl_course (course) VALUES ('"+course+"')"
        c.execute(sql)
        print("inserted successfully")
        conn.commit()
    return 'OK'


def student_registration(firstname, lastname, email, phone, dob, course, semester, joining, leaving, username, password):
    c, conn = connection()
    sql1 = "INSERT INTO tbl_studentregistration (first_name, last_name, email, phone, date_of_birth, course, semester, joining_date, leaving_date, username, password) VALUES ('" + \
        firstname+"','"+lastname+"','"+email+"', "+phone+", '"+dob+"', '"+course+"', " + \
        semester+", '"+joining+"', '"+leaving+"', '"+username+"', '"+password+"')"
    sql2 = "INSERT INTO tbl_login (username, password, type,status) VALUES ('" + \
        username+"','"+password+"','student','Not Verified')"
    print(sql1)
    c.execute(sql1)
    c.execute(sql2)
    print(sql2)
    print("inserted successfully")
    conn.commit()
    return 'OK'
    # uname=request.form["uname"]
    # paswd=request.form["psw"]


def db_dropdown():
    c, conn = connection()
    sql = "select * from tbl_subject"
    c.execute(sql)
    list_tested = c.fetchall()
    print(list_tested)
    return list(list_tested)


def db_dropdowncourse():
    c, conn = connection()
    sql = "SELECT  course_id,course FROM tbl_course"
    c.execute(sql)
    list_tested = c.fetchall()
    print(list_tested)
    return list(list_tested)


def getsub(a):
    c, conn = connection()
    sql = "select question,weight_of_question from tbl_addquestions where subject_id='"+a+"'"
    c.execute(sql)
    list_tested = c.fetchall()
    print(list_tested)
    return list(list_tested)


def getstd(a):
    c, conn = connection()
    sql = "SELECT tbl_studentregistration.student_id, `first_name`, `last_name`, `email`, `phone`, `date_of_birth`, tbl_course.course, tbl_semester.semester, `joining_date`, `leaving_date` FROM `tbl_studentregistration`,tbl_course,tbl_semester,tbl_login where tbl_course.course_id=tbl_studentregistration.course and tbl_semester.semester_id=tbl_studentregistration.semester and tbl_semester.semester_id= '" + \
        str(a) + "' and tbl_login.status='Not Verified' and tbl_login.student_id=tbl_studentregistration.student_id"
    c.execute(sql)
    list_tested = c.fetchall()
    print(list_tested)
    return list(list_tested)


def approve(a):
    c, conn = connection()
    sql = "update tbl_login set status='Verified' where student_id='" + \
        str(a)+"'"
    c.execute(sql)
    conn.commit()
    return '1'


def reject(a):
    c, conn = connection()
    sql = "update tbl_login set status='Rejected' where student_id='" + \
        str(a)+"'"
    c.execute(sql)
    conn.commit()
    return '1'


def db_semester(a):
    c, conn = connection()
    sql = "select semester,semester_id from tbl_semester where cousre_id='"+a+"'"
    c.execute(sql)
    list_tested = c.fetchall()
    print(list_tested)
    return list(list_tested)


def db_subjects(a):
    c, conn = connection()
    sql = "select subject_id,subject from tbl_subject where semester_id='"+a+"'"
    c.execute(sql)
    list_tested = c.fetchall()
    print(list_tested)
    return list(list_tested)


def db_saveanswer(a, c1, d, e, f, g):
    c, conn = connection()
    sql = "INSERT INTO tbl_exam1 (qpcode, question_id, question, weight_of_question, student_id, answer) VALUES ('" + \
        str(c1)+"','"+str(g)+"','"+str(e)+"','" + \
        str(f)+"','"+str(d)+"','"+str(a)+"')"
    print(sql)
    c.execute(sql)
    print("inserted successfully")
    conn.commit()
    return 'OK'


def db_subjectcreateqp(a):
    c, conn = connection()
    sql = "select subject_id,subject from tbl_subject where semester_id='"+a+"'"
    c.execute(sql)
    test = c.fetchall()
    print(test)
    return list(test)


def db_weight(a):
    c, conn = connection()
    sql = "select weight from tbl_weight where subject_id='"+a+"'"
    c.execute(sql)
    test = c.fetchall()
    print(test)
    return list(test)


def getmarks(a):
    c, conn = connection()
    #sql = "select sum(weight*no) from tbl_qpweight where subject_id=%s"
    # sql = "SELECT SUM(weight * no) FROM tbl_qpweight WHERE subject_id = %s"
    sql = "select sum(weight*no) from tbl_qpweight where subject_id='"+a+"'"
    print(f"Executing SQL: {sql} with subject_id={a}")
    c.execute(sql)
    test = c.fetchall()
    print(f"Result from getmarks: {test}")
    return list(test)

def getexam(a):
    c, conn = connection()
    sql = "select nameqp from tbl_questionpaper where qpcode='"+a+"'"
    c.execute(sql)
    test = c.fetchall()
    print(test)
    return list(test)


def getsubject(a):
    c, conn = connection()
    sql = "select subject from tbl_subject where subject_id='"+a+"'"
    c.execute(sql)
    test = c.fetchall()
    print(test)
    return list(test)


def getstud(a):
    c, conn = connection()
    sql = "select email from tbl_studentregistration where semester='"+a+"'"
    c.execute(sql)
    test = c.fetchall()
    print(test)
    return list(test)


def getqp(a):
    c, conn = connection()
    sql = "select qpcode from tbl_questionpaper where subject_id='"+a+"'"
    c.execute(sql)
    test = c.fetchall()
    print(test)
    return list(test)


def getstdmark(a):
    c, conn = connection()
    sql = "select sum(mark),student_id from tbl_exam1 where qpcode='" + \
        a+"' group by student_id"
    c.execute(sql)
    test = c.fetchall()
    print(test)
    return list(test)


def getemail(a):
    c, conn = connection()
    sql = "select email from tbl_studentregistration where student_id='" + \
        str(a)+"'"
    c.execute(sql)
    test = c.fetchall()
    print(test)
    return list(test)


def db_subject():
    c, conn = connection()
    sql = "select subject from tbl_subject"
    c.execute(sql)
    list_tested = c.fetchall()
    print(list_tested)
    return list(list_tested)


def getquestions():
    c, conn = connection()
    sql = "select * from tbl_addquestions"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    return list(data)


def studentexamhome(otp):
    c, conn = connection()
    sql = "select * from tbl_savequestions where qpcode='"+otp+"'"
    c.execute(sql)
    data = c.fetchall()
    # sql1="INSERT INTO tbl_exam (qpcode, question_id, answer) VALUES ('"+qpcode+"','"+question_id+"','"+answer+"')"
    # c.execute(sql1)
    # conn.commit()
    print(data)
    return list(data)



def viewmodelquestions(qpcode, course, semester, subject):
    c, conn = connection()
    #below comment can be excluded
    # sql1="SELECT question,weight_of_question FROM `tbl_addquestions` WHERE subject_id='"+subject+"'"
    #old
    # c.execute("select weight,no from tbl_qpweight where subject_id='"+subject+"'")
    # temp = c.fetchall()
    
    #new
    # Fetch weights and number of questions from tbl_qpweight
    c.execute("SELECT weight, no FROM tbl_qpweight WHERE subject_id = %s", (subject,))
    weights = c.fetchall()
    for weight, num_questions in weights:
        # Fetch random questions based on weight and limit
        sql = "SELECT question_id, question, weight_of_question FROM tbl_addquestions WHERE subject_id = %s AND weight_of_question = %s ORDER BY RAND() LIMIT %s"
        c.execute(sql, (subject, weight, num_questions))
        questions = c.fetchall()

        # Insert selected questions into tbl_savequestions
        for question_id, question, weight_of_question in questions:
            sql_insert = "INSERT INTO tbl_savequestions (qpcode, question_id, question, weight_of_question) VALUES (%s, %s, %s, %s)"
            c.execute(sql_insert, (qpcode, question_id, question, weight_of_question))
            conn.commit()

    # Retrieve questions from tbl_savequestions
    c.execute("SELECT question, weight_of_question FROM tbl_savequestions WHERE qpcode = %s ORDER BY weight_of_question", (qpcode,))
    res = c.fetchall()

    conn.close()  # Close database connection

    return res


    

def generatequestions(qpcode, course, semester, subject, nameqp, duration):
    c, conn = connection()
    # sql1="SELECT t.question,t.weight_of_question FROM tbl_addquestions AS t WHERE t.subject_id='"+subject+"' ORDER BY RAND() LIMIT 1"
    # c.execute(sql1)
    # data = c.fetchall()
    # data=list(data)
    sql2 = "INSERT INTO tbl_questionpaper (qpcode, course_id, semester_id, subject_id,nameqp,duration) VALUES ('" + \
        qpcode+"','"+course+"','"+semester+"', '"+subject + \
        "','"+str(nameqp)+"','"+str(duration)+"')"
    print(sql2)
    c.execute(sql2)
    print("inserted successfully")
    conn.commit()
    conn.close()  # Close database connection
    return "OK"


def studentinfolog():
    c, conn = connection()
    sql = "select * from tbl_studentregistration"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    return list(data)


def loginfo():
    c, conn = connection()
    sql = "select * from tbl_login"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    return list(data)


def seequestions():
    c, conn = connection()
    sql = "select * from tbl_addquestions"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    return list(data)


def courseinfo():
    c, conn = connection()
    sql = "select * from tbl_course"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    return list(data)


def semesterinfo():
    c, conn = connection()
    sql = "select * from tbl_semester"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    return list(data)


def subjectinfo():
    c, conn = connection()
    sql = "select * from tbl_subject"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    return list(data)


def studentsearch():
    c, conn = connection()
    sql = "select * from tbl_studentregistration"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    return list(data)


def viewstudentsearch(student_id):
    c, conn = connection()
    sql = "select * from tbl_studentregistration where student_id='"+student_id+"'"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    return list(data)


def check_qpcode(qpcode):

    print("qpcode")
    c, conn = connection()
    query_string = "select * from tbl_questionpaper where qpcode='"+qpcode+"'"
    print(query_string)
    c.execute(query_string)
    data = c.fetchall()
    if len(data) == 1:
        return (["true", data[0][1]])
        print("success")
    else:
        return (["false"])


def check_otp(otp):

    print("checking otp")
    c, conn = connection()
    query_string = "select * from tbl_questionpaper where qpcode='"+otp+"'"
    print(query_string)
    c.execute(query_string)
    data = c.fetchall()
    if len(data) == 1:
        return (["true", data[0][1]])
        print("success")
    else:
        return (["false"])


def stud_update(student_id, firstname, lastname, email, phone, dob, course, semester, joining, leaving, username, password):
    c, conn = connection()
    sql1 = "UPDATE tbl_studentregistration SET first_name='"+firstname+"', last_name='"+lastname+"' ,email='"+email+"' ,phone="+phone+" ,date_of_birth='"+dob+"' ,course='" + \
        course+"' ,semester="+semester+" ,joining_date='"+joining+"', leaving_date='"+leaving + \
        "', username='"+username+"', password='" + \
        password+"' WHERE student_id='"+student_id+"'"
    print(sql1)
    c.execute(sql1)
    print("Updated successfully")
    conn.commit()
    return 'OK'


def compare_answer(otp, username):
    print(otp)
    print(username)
    c, conn = connection()
    sql1 = "SELECT tbl_addquestions.answer, tbl_exam1.answer,tbl_addquestions.question_id FROM tbl_addquestions, tbl_exam1 WHERE tbl_addquestions.question_id=tbl_exam1.question_id AND tbl_exam1.qpcode='" + \
        str(otp)+"' AND tbl_exam1.student_id='"+str(username)+"'"
    print(sql1)
    c.execute(sql1)
    print("Inserted succesfully")
    data = c.fetchall()
    print(data)
    return (["true", data])


def update_result(otp, username, result, question_id):
    c, conn = connection()
    c.execute(
        "select weight_of_question from tbl_addquestions where question_id='"+str(question_id)+"'")
    res = c.fetchone()
    print(res[0])
    print(result)
    sql1 = "UPDATE tbl_exam1 SET mark='"+str(result*res[0])+"' WHERE qpcode='"+str(
        otp)+"' AND student_id='"+str(username)+"' and question_id='"+str(question_id)+"'"
    print(sql1)
    c.execute(sql1)
    print("Updated successfully")
    conn.commit()
    return 'OK'
