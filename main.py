from decimal import Decimal
from flask import Flask, render_template, request, redirect
from flask import Flask, session
from flask_session import Session
from flask_mail import Mail, Message
from flask import request
from markupsafe import escape
import datetime
import db_connection as db
import nlmodel as nl

app = Flask(__name__, static_url_path='/static')
# app.debug = True
app.secret_key = "sk"
app.config['SESSION_TYPE'] = 'filesystem'
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "smartexams2k24@gmail.com",
    "MAIL_PASSWORD": "zyul fkmc iyce mhxr"
}
Session(app)
app.config.update(mail_settings)

TEMPLATES_AUTO_RELOAD = True
db.connection()


@app.route("/login")
def hello():
    return render_template("index.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/icons")
def icons():
    return render_template("icons.html")


@app.route("/typography")
def typography():
    return render_template("typography.html")


@app.route("/mail")
def mail():
    return render_template("mail.html")


@app.route("/register")
def register():
    course = db.db_dropdowncourse()
    return render_template("registration.html", course=course)


@app.route("/Addquestions")
def Addquestions():
    temp = db.db_dropdowncourse()
    return render_template("adminaddqp.html", abc=temp)


@app.route("/Createquestions")
def Createquestions():
    temp = db.db_dropdowncourse()
    print(temp)
    return render_template("admingetqp.html", abc=temp)


@app.route("/Results")
def Results():
    temp = db.db_dropdowncourse()
    return render_template("adminresult.html", abc=temp)


@app.route("/Showquestions")
def Showquestions():
    temp1 = db.db_dropdowncourse()
    return render_template("adminshowquestions.html", abc=temp1)


@app.route("/Studentreg")
def Studentreg():
    course = db.db_dropdowncourse()
    return render_template("verify.html", course=course)


@app.route("/Previousqp")
def Previousqp():
    return render_template("adminpreviousqp.html")


@app.route("/Update")
def Update():
    return render_template("adminhome.html")


@app.route("/studentexamhome")
def Studentexamhome():
    return render_template("studentexamhome.html")


@app.route("/setsem", methods=['POST'])
def setsem():
    a = request.form['key']
    print(a)
    insert_status = db.db_semester(a)
    print(insert_status)
    b = '<select name="sem" class="form-control" id="semester" onchange="setsub(this.value)">'
    b = b+'<option value="" >--select--</option>'
    for a in insert_status:
        b = b+'<option value="'+str(a[1])+'">'+str(a[0])+'</option>\n'
    b = b+'</select>'
    print(b)
    return (b)


@app.route("/setsemv", methods=['POST'])
def setsemv():
    a = request.form['key']
    print(a)
    insert_status = db.db_semester(a)
    print(insert_status)
    b = '<select name="sem" class="form-control" id="semester" onchange="getstd(this.value)">'
    b = b+'<option value="" >--select--</option>'
    for a in insert_status:
        b = b+'<option value="'+str(a[1])+'">'+str(a[0])+'</option>\n'
    b = b+'</select>'
    print(b)
    return (b)


@app.route("/setsemadd", methods=['POST'])
def setsemadd():
    a = request.form['key']
    print(a)
    insert_status = db.db_semester(a)
    print(insert_status)
    b = '<select name="sem" class="form-control" id="semester" onchange="getsub(this.value)">'
    b = b+'<option value="" >--select--</option>'
    for a in insert_status:
        b = b+'<option value="'+str(a[1])+'">'+str(a[0])+'</option>\n'
    b = b+'</select>'
    print(b)
    return (b)


@app.route("/getsub", methods=['POST'])
def getsub():
    a = request.form['key']
    print(a)
    insert_status = db.db_subjects(a)
    print(insert_status)
    b = '<select name="sub" class="form-control" id="sub" >'
    b = b+'<option value="" >--select--</option>'
    for a in insert_status:
        b = b+'<option value="'+str(a[0])+'">'+str(a[1])+'</option>\n'
    b = b+'</select>'
    print(b)
    return (b)


@app.route("/getstd", methods=['POST'])
def getstd():
    a = request.form['key']
    print(a)
    res = db.getstd(a)
    print(res)
    b = """<table id="bootstrap-data-table" class="table table-striped table-bordered">


                                    <thead>
                                        <tr>
                                          <th>Student Id</th>
                                            <th>Student Name</th>
                                          
                                            <th>Email</th>
                                            <th>Phone</th>
					    <th>DOB</th>
					    <th>Course</th>
					    <th>Semester</th>
					    <th>Join Date</th>
					    <th>Leaving Date</th>
					    <th>Verify</th>
                                        </tr>
                                    </thead>
                                    <tbody>"""
    for a in res:
        b = b+"<tr><td>"+str(a[0])+"</td>"
        b = b+"<td>"+str(a[1]) + " " + str(a[2])+"</td>"
        b = b+"<td>"+str(a[3])+"</td>"
        b = b+"<td>"+str(a[4])+"</td>"
        b = b+"<td>"+str(a[5])+"</td>"
        b = b+"<td>"+str(a[6])+"</td>"
        b = b+"<td>"+str(a[7])+"</td>"
        b = b+"<td>"+str(a[8])+"</td>"
        b = b+"<td>"+str(a[9])+"</td>"
        b = b+"""<td><button onclick="change("""+str(
            a[0])+""",'approve')">Approve</button>&nbsp;<button onclick="change("""+str(a[0])+""",'reject')">Reject</a></button>"""
    b = b+"""  </tbody>
                                </table>"""

    print(b)
    return (b)


@app.route("/change", methods=['POST', 'GET'])
def approve():
    a = request.form['stdid']
    b = request.form['status']
    print(b)
    if (b == "approve"):
        x = db.approve(a)
    else:
        x = db.reject(a)
    return "ok"


@app.route("/reject/<string:student_id>", methods=['POST', 'GET'])
def reject(student_id):
    a = db.reject(student_id)
    return render_template("verify.html")


@app.route("/setsub", methods=['POST'])
def setsub():
    a = request.form['key']
    print(a)
    insert_status = db.db_subjectcreateqp(a)
    print(insert_status)
    b = '<select name="sub" class="form-control" id="subject" >'
    b = b+'<option value="" >--select--</option>'
    for a in insert_status:
        b = b+'<option value="'+str(a[0])+'">'+str(a[1])+'</option>\n'
    b = b+'</select>'
    print(b)

    return (b)


@app.route("/setqp", methods=['POST'])
def setqp():
    a = request.form['key']
    print(a)
    insert_status = db.getqp(a)
    print(insert_status)
    b = '<select name="qpcode" class="form-control" id="qpcode" >'
    b = b+'<option value="" >--select--</option>'
    for a in insert_status:
        b = b+'<option value="'+str(a[0])+'">'+str(a[0])+'</option>\n'
    b = b+'</select>'
    print(b)

    return (b)


@app.route("/setsub2", methods=['POST'])
def setsub2():
    a = request.form['key']
    print(a)
    insert_status = db.db_subjectcreateqp(a)
    print(insert_status)
    b = '<select name="sub" class="form-control" id="subject" onchange="setqp(this.value)" >'
    b = b+'<option value="" >--select--</option>'
    for a in insert_status:
        b = b+'<option value="'+str(a[0])+'">'+str(a[1])+'</option>\n'
    b = b+'</select>'
    print(b)

    return (b)


@app.route("/setweight", methods=['POST'])
def setweight():
    a = request.form['key']
    print(a)
    insert_status = db.db_weight(a)
    print(insert_status)
    b = '<select name="weight" class="form-control" id="weight" >'
    b = b+'<option value="" >--select--</option>'
    for a in insert_status:
        b = b+'<option value="'+str(a[0])+'">'+str(a[0])+'</option>\n'
    b = b+'</select>'
    print(b)

    return (b)


@app.route("/setsub1", methods=['POST'])
def setsub1():
    a = request.form['key']
    print(a)
    insert_status = db.db_subjectcreateqp(a)
    print(insert_status)
    b = '<select name="sub" class="form-control" id="subject" onchange="setweight(this.value)" >'
    b = b+'<option value="" >--select--</option>'
    for a in insert_status:
        b = b+'<option value="'+str(a[0])+'">'+str(a[1])+'</option>\n'
    b = b+'</select>'
    print(b)

    return (b)
    # return render_template("studentexamhome.html")


@app.route("/answer", methods=['POST'])
def answer():
    a = request.form['key']
    c = request.form['c']
    d = request.form['d']
    e = request.form['e']
    f = request.form['f']
    g = request.form['g']
    print(a)
    print(c)
    print(g)
    insert_status = db.db_saveanswer(a, c, d, e, f, g)
    # print(insert_status)
    # b='<select name="sem" id="semester" onchange="setsub(this.value)">'
    # '<option value="" >--select--</option>'
    # for a in insert_status:
    # 	b=b+'<option value="'+str(a[1])+'">'+str(a[0])+'</option>\n'
    # b=b+'</select>'
    # print(b)
    return ("dfdg")


@app.route("/login1")
def login1():
    return render_template("login.html")


@app.route("/check_login", methods=['POST', 'GET'])
def check_login():
    print("insert data")
    uname = request.form["uname"]
    print(uname)

    paswd = request.form["pword"]
    status = db.check_login(uname, paswd)
    if status[0] == "true":
        session['student_id'] = status[1]
        if status[3] == "admin":
            username = session['student_id']
            return render_template("adminhome.html", a1=username)
        if status[3] == "student":
            username = session['student_id']
            return render_template("otp.html", a1=username)
    else:
        print("false")
        return render_template("login.html")


@app.route("/stud_instr", methods=['POST', 'GET'])
def stud_instr():
    otp = request.form["otp"]
    print(otp)
    status = db.check_otp(otp)
    if status[0] == "true":
        return render_template("studentinstruction.html", e=otp)
    else:
        return render_template("otp.html")


@app.route("/stud_home/<string:otp>", methods=['POST', 'GET'])
def stud_home(otp):
    temp1 = db.studentexamhome(otp)
    username = session['student_id']
    return render_template("studentexamhome.html", abc=temp1, e=otp, a1=username)


@app.route("/addcourse", methods=['POST', 'GET'])
def addcourse():
    return render_template("addcourse.html")


@app.route("/addcoursesave", methods=['POST', 'GET'])
def addcoursesave():
    course = request.form["course"]
    insert_status = db.addcourse(course)
    return render_template("adminhome.html")


@app.route("/addsem", methods=['POST', 'GET'])
def addsem():
    data = db.db_dropdowncourse()
    return render_template("addsem.html", abc=data)


@app.route("/addsemsave", methods=['POST', 'GET'])
def addsemsave():
    course = request.form["course"]
    sem = request.form["sem"]
    insert_status = db.addsem(course, sem)
    return render_template("adminhome.html")


@app.route("/addsub", methods=['POST', 'GET'])
def addsub():
    data = db.db_dropdowncourse()
    return render_template("addsub.html", abc=data)


@app.route("/sendqp", methods=['POST', 'GET'])
def sendqp():
    data = db.db_dropdowncourse()
    return render_template("sendqpcode.html", abc=data)


@app.route("/addsubsave", methods=['POST', 'GET'])
def addsubsave():
    course = request.form["course"]
    sem = request.form["sem"]
    sub = request.form["sub"]
    insert_status = db.addsub(course, sem, sub)
    return render_template("adminhome.html")


@app.route("/addweight", methods=['POST', 'GET'])
def addweight():
    data = db.db_dropdowncourse()
    return render_template("addweight.html", abc=data)


@app.route("/addweightsave", methods=['POST', 'GET'])
def addweightsave():
    course = request.form["crc"]
    sem = request.form["sem"]
    sub = request.form["sub"]
    weight = request.form["weight"]
    insert_status = db.addweight(course, sem, sub, weight)
    return render_template("adminhome.html")


@app.route("/qpset", methods=['POST', 'GET'])
def qpset():
    data = db.db_dropdowncourse()
    return render_template("qpsetting.html", abc=data)


@app.route("/qpsetsave", methods=['POST', 'GET'])
def qpsetsave():
    course = request.form["crc"]
    sem = request.form["sem"]
    sub = request.form["sub"]
    weight = request.form["weight"]
    no = request.form["no"]
    insert_status = db.qpset(course, sem, sub, weight, no)
    return render_template("adminhome.html")


@app.route("/add_questions", methods=['POST', 'GET'])
def add_questions():
    subjectid = request.form["sub"]
    question = request.form["qus"]
    answer = request.form["ans"]
    keyanswer = request.form["keyans"]
    weight = request.form["weight"]
    date = str(datetime.date.today())
    insert_status = db.add_questions(
        subjectid, question, answer, keyanswer, weight, date)
    return render_template("adminhome.html")


@app.route("/sendqpcode", methods=['POST', 'GET'])
def sendqpcode():
    subjectid = request.form["sub"]
    semester = request.form["sem"]
    qpcode = request.form["qpcode"]
    exam = db.getexam(qpcode)
    subject = db.getsubject(subjectid)
    res = db.getstud(semester)
    print(res)
    for i in res:
        mail = Mail(app)
        msg = Message(subject="Exam OTP",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[i[0]],
                      body="OTP for the Examination \n Exam : "+str(exam[0]) + "\n Subject : "+str(subject[0])+"\n OTP : "+str(qpcode))
        mail.send(msg)
    return render_template("adminhome.html")


@app.route("/sendresult", methods=['POST', 'GET'])
def sendresult():
    subjectid = request.form["sub"]
    semester = request.form["sem"]
    qpcode = request.form["qpcode"]
    exam = db.getexam(qpcode)
    subject = db.getsubject(subjectid)
    res = db.getstdmark(qpcode)
    print(res)
    for i in res:
        email = db.getemail(i[1])
        print(email[0][0])

        mail = Mail(app)
        msg = Message(subject="Exam Result",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[email[0][0]],
                      body="Result of the Examination \n Exam : "+str(exam[0]) + "\n Subject : "+str(subject[0])+"\n Mark : "+str(i[0]))
        mail.send(msg)
    return render_template("adminhome.html")


@app.route("/student_registration", methods=['POST', 'GET'])
def student_registration():
    firstname = request.form["fname"]
    lastname = request.form["lname"]
    email = request.form["email"]
    phone = request.form["phone"]
    dob = request.form["dob"]
    course = request.form["cname"]
    semester = request.form["sem"]
    joining = request.form["joinday"]
    leaving = request.form["endday"]
    username = request.form["studentuname"]
    password = request.form["studentpsword"]
    insert_status = db.student_registration(
        firstname, lastname, email, phone, dob, course, semester, joining, leaving, username, password)
    if (insert_status):
        mail = Mail(app)
        msg = Message(subject="Registration Successfuly Completed",
                      sender=app.config.get("MAIL_USERNAME"),
                      # replace with your email for testing
                      recipients=[email],
                      body="Your Login Credentials for Smart Exam is Username : "+username+" Password : "+password)
        mail.send(msg)
    return render_template("index.html")


@app.route("/viewmodelquestions", methods=['POST'])
def viewmodelquestions():
    try:
        course = request.form["crc"]
        semester = request.form["sem"]
        subject = request.form["sub"]
        nameqp = request.form["nameqp"]
        qpcode = request.form["qpcode"]
        duration = request.form["duration"]
        a = request.form["a"]
        date = str(datetime.date.today())

        print(f"Course: {course}")
        print(f"Semester: {semester}")
        print(f"Subject: {subject}")
        print(f"A: {a}")

        status = db.check_qpcode(qpcode)
        print(f"Status: {status}")

        if not status or len(status) == 0:
            print("Empty status returned.")
            return "<h3>Invalid status or empty status returned.</h3>"

        status_value = status[0]
        print(f"Status value: {status_value}")

        if a == "2":
            res = db.getmarks(a)
            print(f"Marks: {res}")
            total_marks = res
            
            print(f"Total marks type: {type(total_marks)}, value: {total_marks}")
            c1 = """<center></center><div align="right">Reg. No................
</div>
<h3><center>{}</center></h3><br><br>
<div ALIGN=LEFT>Time: {} hrs</div><div ALIGN=RIGHT>Marks: {}</div>
<br><center>Answer all questions in this section</center><br>
<hr>""".format(nameqp, duration, total_marks)

            
            temp1 = db.viewmodelquestions(qpcode, course, semester, a)
            print(f"Questions from db.viewmodelquestions: {temp1}")

            # if not temp1:
            #     print("No questions found in temp1.")
            #     return "<h3>No questions found for the provided criteria.</h3>"

            for question in temp1:
                if len(question) >= 2:
                    c1 =c1+ "<h5>{}&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp{}</h5><br>".format(question[0], question[1])
                else:
                    print(f"Invalid question format: {question}")
            print(c1)
            return c1

        if status_value == "true":
            return "1"
        if a == "1" and status_value == "false":
            temp1 = db.generatequestions(qpcode, course, semester, subject, nameqp, duration)
            c = "<h3>Question Paper is generated with {} as question paper code</h3><br>".format(qpcode)
            print(c)
            return c
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"

    
    

@app.route("/logout")
def logout():
    return render_template("login.html")


@app.route("/datatables", methods=['POST', 'GET'])
def datatables():
    temp1 = db.studentinfolog()
    return render_template("tables-data.html", abc=temp1)


@app.route("/loginfo", methods=['POST', 'GET'])
def loginfo():
    temp1 = db.loginfo()
    return render_template("studentloginfo.html", abc=temp1)


@app.route("/seequestions", methods=['POST', 'GET'])
def seequestions():
    temp1 = db.seequestions()
    return render_template("adminseequestions.html", abc=temp1)


@app.route("/courseinfo", methods=['POST', 'GET'])
def courseinfo():
    temp1 = db.courseinfo()
    return render_template("admincourseinfo.html", abc=temp1)


@app.route("/semesterinfo", methods=['POST', 'GET'])
def semesterinfo():
    temp1 = db.semesterinfo()
    return render_template("adminsemesterinfo.html", abc=temp1)


@app.route("/subjectinfo", methods=['POST', 'GET'])
def subjectinfo():
    temp1 = db.semesterinfo()
    return render_template("adminsubjectinfo.html", abc=temp1)


@app.route("/studentsearch", methods=['POST', 'GET'])
def studentsearch():
    temp1 = db.studentsearch()
    return render_template("newsearchstudent.html", abc=temp1)


@app.route("/viewstudentsearch/<string:student_id>", methods=['POST', 'GET'])
def viewstudentsearch(student_id):
    temp1 = db.viewstudentsearch(student_id)
    return render_template("viewstudent.html", e=temp1)


@app.route("/edit_student/<string:student_id>", methods=['POST', 'GET'])
def editstudent(student_id):
    temp1 = db.viewstudentsearch(student_id)
    return render_template("reg.html", e=temp1)


@app.route("/stud_update/<string:student_id>", methods=['POST', 'GET'])
def stud_update(student_id):
    firstname = request.form["fname"]
    lastname = request.form["lname"]
    email = request.form["email"]
    phone = request.form["phone"]
    dob = request.form["dob"]
    course = request.form["cname"]
    semester = request.form["sem"]
    joining = request.form["joinday"]
    leaving = request.form["endday"]
    username = request.form["studentuname"]
    password = request.form["studentpsword"]
    update_status = db.stud_update(student_id, firstname, lastname, email,
                                   phone, dob, course, semester, joining, leaving, username, password)
    return render_template("adminhome.html")


@app.route("/cosine", methods=['POST'])
def cosine():
    c = request.form['c']
    username = session['student_id']
    print(c)
    print(username)
    temp1 = db.compare_answer(c, username)
    # print("ivade nokkedo==============================")
    print(temp1)
    if temp1[0] == "true":
        for a1 in temp1[1]:
            # print("hallooooooooooooooooooooooooooooooooooooooooooooo")
            print(a1[0])
            a = nl.removestop_words(str(a1[0]), str(a1[1]))
            print("af1", a["f1"])
            print("af2", a["f2"])
            result = nl.get_cosine_similarity(a["f1"], a["f2"])
            print(result)
            update_result = db.update_result(c, username, result, a1[2])
    return render_template("adminhome.html")


@app.route("/viewquestions", methods=['POST'])
def viewquestions():
    a = request.form['sub']
    print(a)
    insert_status = db.getsub(a)
    print(insert_status)
    b = "<p>"
    # b=b+"<h5>Question &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp Weightage </h2><br></br>"
    for a in insert_status:
        b = b+"<h5>" + \
            str(a[0])+" &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" + \
            str(a[1])+" </h2><br></br>"
    b = b+"</p>"
    print(b)

    return (b)


if __name__ == "__main__":
    app.run()
