from django.shortcuts import render,redirect
import sqlite3

username=[]
course=''
type_=''

def login_home(request):
    global username
    global course

    if len(request.GET.keys())==0:
        return render(request, 'Login.html')
    else:
        req=request.GET
        db = sqlite3.connect('cms_database.db')
        cursor = db.cursor()
        print('\n\n',req,'\n\n')
        cursor.execute(f"SELECT sid,password FROM Student where sid='{req['uname']}' and password='{req['pass']}'")
        all_rows = cursor.fetchall()
        print('\n\n',all_rows)
        
        if len(all_rows)>0:
            username=req['uname']
            type_=0
            request.GET={}
            return redirect('http://127.0.0.1:8000/dashboard')
        else:
            cursor.execute(f"SELECT tid,password FROM teacher where tid='{req['uname']}' and password='{req['pass']}'")
            all_rows = cursor.fetchall()
            print('\n\n',all_rows)
            db.close()
            if len(all_rows)>0:
                username=req['uname']
                type_=1
                request.GET={}
                return redirect('http://127.0.0.1:8000/dashboard1')
            else:
                return render(request, 'Login(fail).html')

    print('\n\n',request.GET,'\n\n')
    

def signUp(request):
    global username
    global course
    return render(request, 'SignUp.html')

def quiz(request):
    global username
    global course
    return render(request, 'Quiz.html')

def schedule(request):
    global username
    global course

    if len(request.GET.keys())==0:
        return render(request, 'Schedule(Student).html')
    else:
        req=request.GET
        db = sqlite3.connect('cms_database.db')
        cursor = db.cursor()
        print('\n\n',req,'\n\n')
        q=f"insert into appointment values('{username}','{req['day']} {req['time']}','{course[3]}')"
        print(q)
        cursor.execute(q)
        db.commit()
        db.close()
        return redirect('http://127.0.0.1:8000/dashboard')

def discussion(request):
    global username
    global course
    return render(request, 'Discussion.html')

def logout(request):
    global username
    global course
    username.pop()
    return render(request, 'Login.html')

def marks(request):
    global username
    global course

    print(request)
    db = sqlite3.connect('cms_database.db')
    cursor = db.cursor()
    q=f"SELECT course.cname,coursemarks3.midsem,coursemarks3.compre from coursemarks3,course where coursemarks3.sid='{username}' and coursemarks3.cid=course.cid"
    print('----',q)
    cursor.execute(q)
    all_rows = cursor.fetchall()
    
    dict1={i:all_rows[i] for i in range(len(all_rows))}
    
    print(dict1)
    db.close()
    return render(request, 'Marks.html',{'dict1':all_rows})

def marks1(request):
    global username
    global course

    print(request)
    db = sqlite3.connect('cms_database.db')
    cursor = db.cursor()
    q=f"SELECT coursemarks3.cid,coursemarks3.sid,coursemarks3.midsem,coursemarks3.compre from coursemarks3,course,teacher where teacher.tid='{username}' and teacher.tid=course.tid and coursemarks3.cid=course.cid"
    print('----',q)
    cursor.execute(q)
    all_rows = cursor.fetchall()
    
    dict1={i:all_rows[i] for i in range(len(all_rows))}
    
    print(dict1)
    db.close()
    return render(request, 'Marks1.html',{'dict1':all_rows})
    
def enroll_course(request):
    global username
    global course


    return render(request, 'enroll_course.html')

def feedback(request):
    global username
    global course

    if len(request.GET.keys())==0:
        return render(request, 'Feedback.html')
    else:
        req=request.GET
        db = sqlite3.connect('cms_database.db')
        cursor = db.cursor()
        print('\n\n',req,'\n\n')
        q=f"insert into coursefeedback values('{course[0]}','{req['feedback']}')"
        print(q)
        cursor.execute(q)
        db.commit()
        db.close()
        return redirect('http://127.0.0.1:8000/dashboard')

def course(request):
    global username
    global course
    # req=request.GET

    # db = sqlite3.connect('cms_database.db')
    # cursor = db.cursor()
    # print('\n\n',req,'\n\n')
    # cursor.execute(f"SELECT sid,password FROM Student where sid='{req['uname']}' and password='{req['pass']}'")
    # all_rows = cursor.fetchall()
    # print('\n\n',all_rows)
    # db.close()
    # if len(all_rows)>0:
    #     username=req['uname']
    #     request.GET={}
    #     return redirect('http://127.0.0.1:8000/dashboard')
    # else:
    #     return render(request, 'Login(fail).html')

    return render(request, 'Course.html')

def dashboard1(request):
    global username
    global course

    print(request)
    db = sqlite3.connect('cms_database.db')
    cursor = db.cursor()
    q=f"SELECT course.cid,course.cname FROM course,teacher where teacher.tid='{username}' and teacher.tid=course.tid"
    print('----',q)
    cursor.execute(q)
    all_rows = cursor.fetchall()
    course=all_rows[0]
    dict1={i:all_rows[i] for i in range(len(all_rows))}
    
    print(dict1)
    db.close()
    return render(request, 'Dashboard1.html',{'dict1':all_rows})
    
def dashboard(request):
    global username
    global course

    print(request)
    db = sqlite3.connect('cms_database.db')
    cursor = db.cursor()
    q=f"SELECT course.cid,course.cname,teacher.tname,course.tid FROM course,studentcourse,teacher where studentcourse.sid='{username}' and studentcourse.cid=course.cid and teacher.tid=course.tid"
    print('----',q)
    cursor.execute(q)
    all_rows = cursor.fetchall()
    course=all_rows[0]
    dict1={i:all_rows[i] for i in range(len(all_rows))}
    
    print(dict1)
    db.close()
    return render(request, 'Dashboard.html',{'dict1':all_rows})
    