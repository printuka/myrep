from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import mysql.connector


def get_name(request):

    template = loader.get_template('myapp/form.html')
    context ={ }

    return HttpResponse(template.render(context,request))


def admin_page(request):
    template = loader.get_template('myapp/admin.html')
    context ={ }

    return HttpResponse(template.render(context,request))


def show(request):
    #name = request.POST['your_name']
    #print(name)
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        passwd='Codes&tide97', #"mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    if request.POST.get("1"):

        mycursor = mydb.cursor()

        mycursor.execute('select * from instructor order by name')

        template = loader.get_template('myapp/table.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("2"):

        mycursor = mydb.cursor()

        mycursor.execute('select * from instructor order by dept_name')

        template = loader.get_template('myapp/table.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("3"):
        
        mycursor = mydb.cursor()

        mycursor.execute('select * from instructor order by salary')

        template = loader.get_template('myapp/table.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("error")
        
def prof_page(request):
    template = loader.get_template('myapp/professor.html')
    context ={ }

    return HttpResponse(template.render(context,request)) 

def semester(request):
    template = loader.get_template('myapp/semester.html')
    context ={ }

    return HttpResponse(template.render(context,request))
    
def semester2(request):
    template = loader.get_template('myapp/semester2.html')
    context ={ }

    return HttpResponse(template.render(context,request)) 

def results(request):
    #name = request.POST['your_name']
    #print(name)
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        passwd='Codes&tide97', #"mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    if request.POST.get("1"):

        mycursor = mydb.cursor()

        mycursor.execute('select takes.course_id, takes.sec_id, takes.year, count(takes.course_id) as "# of students" from takes, teaches where takes.semester=1 and teaches.semester=1 and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year group by takes.course_id')

        template = loader.get_template('myapp/table2.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("2"):

        mycursor = mydb.cursor()

        mycursor.execute('select takes.course_id, takes.sec_id, takes.year, count(takes.course_id) as "# of students" from takes, teaches where takes.semester=2 and teaches.semester=2 and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year group by takes.course_id')

        template = loader.get_template('myapp/table2.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("3"):
        
        mycursor = mydb.cursor()

        mycursor.execute('select takes.course_id, takes.sec_id, takes.year, count(takes.course_id) as "# of students" from takes, teaches where takes.semester=3 and teaches.semester=3 and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year group by takes.course_id')

        template = loader.get_template('myapp/table2.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))  
    else:
        return HttpResponse("error")  

def results2(request):
    #name = request.POST['your_name']
    #print(name)
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        passwd='Codes&tide97', #"mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    if request.POST.get("1"):

        mycursor = mydb.cursor()

        mycursor.execute('select name from takes, student, teaches where takes.semester=1 and teaches.semester=1 and takes.id=student.id and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year')

        template = loader.get_template('myapp/table3.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("2"):

        mycursor = mydb.cursor()

        mycursor.execute('select name from takes, student, teaches where takes.semester=2 and teaches.semester=2 and takes.id=student.id and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year')

        template = loader.get_template('myapp/table3.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("3"):
        
        mycursor = mydb.cursor()

        mycursor.execute('select name from takes, student, teaches where takes.semester=3 and teaches.semester=3 and takes.id=student.id and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year')

        template = loader.get_template('myapp/table3.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))  
    else:
        return HttpResponse("error")         