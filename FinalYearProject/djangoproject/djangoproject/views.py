
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,render
from . forms import *
from . models import *
from .urls import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random


def mainhome(request):
  return render(request,"html/start.html")

def home(request):
  return render(request,"html/start.html")

def adminhome(request):
    ausername=request.session['ausername']
    return render(request,"html/adminhomepage.html",{'ausername':ausername})

def addtest(request):
  return render(request,"html/addtest.html")

def addcourse(request):
  return render(request,"html/addcourse.html")

def courseallocation(request):
    ausername=request.session['ausername']
    Courseallocation = facultycourseallocation.objects.all()
    facultys = faculty.objects.all()
    c = courses.objects.all()

    form = courseAllocationForm
    if request.method == 'POST':
        fusername=request.POST.get('fusername')
        course_code=request.POST.get('course_code')
        course_title=request.POST.get('course_title')
        print(fusername)
        print(course_code)
        print(course_title)
        msg=None
        flag=facultycourseallocation.objects.filter(fusername=fusername)
        flag1=facultycourseallocation.objects.filter(course_code=course_code)
        flag2=facultycourseallocation.objects.filter(course_title=course_title)
        form = courseAllocationForm(request.POST)
        if flag:
            msg = "Faculty is Already Allocated "
            return render(request,'html/courseallocation.html',{'msg':msg,'ausername':ausername,'courses':Courseallocation,'msg':msg,'facultys':facultys,'c':c})
        if flag1:
            msg = "Course is Already Allocated "
            return render(request,'html/courseallocation.html',{'msg':msg,'ausername':ausername,'courses':Courseallocation,'msg':msg,'facultys':facultys,'c':c})
        if flag2:
            msg = "Course is Already Allocated "
            return render(request,'html/courseallocation.html',{'msg':msg,'ausername':ausername,'courses':Courseallocation,'msg':msg,'facultys':facultys,'c':c})
        elif form.is_valid():
            form.save()
            msg="Course allocated Succesfully"
            return render(request,'html/courseallocationok.html',{'msg':msg,'ausername':ausername,'courses':Courseallocation,'facultys':facultys,'c':c})
        else:
            form = courseAllocationForm()
        
    return render(request,'html/courseallocation.html',{'form':form,'ausername':ausername,'courses':Courseallocation,'facultys':facultys,'c':c})

def viewallocated(request):
    fusername = request.session['fusername']
    courseallocation = facultycourseallocation.objects.all()

    return render(request,'html/viewallocated.html',{'fusername':fusername,'courseallocation':courseallocation})


def viewcourses(request):
    susername=request.session['susername']
    Courses = courses.objects.all()
    quizresult = quiz_result.objects.filter(username=susername)
    rating = ratingcourse.objects.all()
    list1=[]
    

    return render(request,'html/viewcourses.html',{'Courses':Courses,'susername':susername,'quizresult':quizresult,'rating':rating})
# 'category':category,'specialization':specialization,'course_code':course_code,'course_title':course_title,'description':description}

def displayquiz(request):
    susername=request.session['susername']
    msg=None
    flag=quiz_result.objects.filter(username=susername)
    if flag:
        msg = "Already Attempted"
        return render(request,'html/savequiz.html',{'flag':flag,'msg':msg})
    else:
        quizqb = questionbank.objects.all()
        form = quizForm()
        return render(request,'html/displayquiz.html',{'form':form,'quizqb':quizqb,'susername':susername})

def savequiz(request):
    susername=request.session['susername']
    msg=None
    flag=quiz_result.objects.filter(username=susername)
    if flag:
        msg = "Already Attempted"
    else:
        if request.method == 'POST':
            data = request.POST
            quizdb = questionbank.objects.all()
            noq = questionbank.objects.count()
            list1=[]
            list2=[]
            list3=[]
            list4=[]

            for question in quizdb:
                category = question.question_rid.split("_")
                print(category[0],category[1])
                print(question.question_rid,'=',request.POST[question.question_rid])
                if category[0]=="EXTROVERTED":
                    list1.append(request.POST[question.question_rid])
                if category[0]=="SENSING":
                    list2.append(request.POST[question.question_rid])
                if category[0]=="THINKING":
                    list3.append(request.POST[question.question_rid])
                if category[0]=="JUDGING":
                    list4.append(request.POST[question.question_rid])
            a1 = list1.count("answer1")
            a2 = list1.count("answer2")
            A3 = list1.count("answer3")
            A4 = list1.count("answer4")
            a3 = 0
            a4 = 0
            b1 = list2.count("answer1")
            b2 = list2.count("answer2")
            B3 = list1.count("answer3")
            B4 = list1.count("answer4")
            b3 = 0
            b4 = 0
            c1 = list3.count("answer1")
            c2 = list3.count("answer2")
            C3 = list1.count("answer3")
            C4 = list1.count("answer4")
            c3 = 0
            c4 = 0
            d1 = list4.count("answer1")
            d2 = list4.count("answer2")
            D3 = list1.count("answer3")
            D4 = list1.count("answer4")
            d3 = 0
            d4 = 0

            label=""
            if(a1>a2 and a1>a3 and a1>a4):
                label=label+"E"
            elif(a2>a1 and a2>a3 and a2>a4):
                label=label+"I"
            else:
                label="none"
            if(b1>b2 and b1>b3 and b1>b4):
                label=label+"S"
            elif(b2>b1 and b2>b3 and b2>b3):
                label=label+"I"
            else:
                label="none"
            if(c1>c2 and c1>c3 and c1>c4):
                label=label+"T"
            elif(c2>c1 and c2>c3 and c2>c4):
                label=label+"F"
            else:
                label="none"            
            if(d1>d2):
                label=label+"J"
            elif(d1>d2 and d1>d3 and d1>d4):
                label=label+"P"
            else:
                label="none"
            specialization=""
            if label=="ISFJ" or label=="EITP" or label=="ESFJ" or label=="IITJ" or label=="IIFP" or label=="ISFP":
                specialization="SECURITY AND FORENSICS"
            elif label=="ESTJ" or label=="ESTP" or label=="ESFP" or label=="IIFJ" or label=="EIFJ":
                specialization="NETWORKING"
            elif label=="ISTJ" or label=="ISTP" or label=="EITJ" or label=="EIFP" or label=="IITP":
                specialization="APP DEVELOPMENT"
            else:
                specialization="Can't be determined"
                

            quizresult = quiz_result() 
            quizresult.username = request.session['susername'] 
            quizresult.label = label
            quizresult.specialization = specialization 
            quizresult.save() 
            msg="Submitted Succesfully" 
            flag=quiz_result.objects.filter(username=susername) 

            temps = temp()
            temps.sname = request.session['susername']
            temps.a1 = a1
            temps.a2 = a2
            temps.a3 = A3
            temps.a4 = A4
            temps.b1 = b1
            temps.b2 = b2
            temps.b3 = B3
            temps.b4 = B4
            temps.c1 = c1
            temps.c2 = c2
            temps.c3 = C3
            temps.c4 = C4
            temps.d1 = d1
            temps.d2 = d2
            temps.d3 = D3
            temps.d4 = D4
            temps.label = label
            temps.specialization = specialization
            temps.save()

        
    return render(request,'html/savequiz.html',{'flag':flag,'msg':msg})

def studentdata(request):
    ausername = request.session['ausername']
    students = student.objects.all()
    temps = temp.objects.all()

    return render(request,'html/studentdata.html',{'students':students,'temps':temps})

       

def registercourses(request,cid):
    susername=request.session['susername']
    Courses = courses.objects.all()
    quizresult = quiz_result.objects.filter(username=susername)
    
    #cid=request.GET["cid"]
    #course = courses.objects.filter(course_id=cid)
    msg=None
    flag=studentregisteredcourses.objects.filter(susername=susername,course_id=cid)

    if flag:
        msg = "Already Registered"
    else:
        courseobjs = courses.objects.all()
        for course in courseobjs:
            if course.course_id==int(cid):
                registeredcourse = studentregisteredcourses()
                registeredcourse.susername=susername
                registeredcourse.course_id=course.course_id
                registeredcourse.course_title=course.course_title
                registeredcourse.course_code=course.course_code
                print(registeredcourse)
                registeredcourse.save()
                msg="registered successfully"
    return render(request,'html/viewcoursesok.html',{'msg':msg,'Courses':Courses,'susername':susername,'quizresult':quizresult})


def courserating(request,ccd):
    susername=request.session['susername']
    if request.method == 'POST':
        form = courseratingForm(request.POST)
        if form.is_valid():
            courseratings = ratingcourse(course_code=ccd,studentusername=susername,rating=form.data['rating'],remarks=form.data['remarks'])
            courseratings.save()
            print(form.data['rating'],form.data['remarks'],ccd)
            return HttpResponse("hy")
    else:
        form = courseratingForm()
    return render(request,'html/courserating.html',{'form':form,'susername':susername,'ccd':ccd})

    
    # coursecode=request.POST.get('ccd')
    # print(coursecode)
    # susername=request.session['susername']
    # if request.method == 'POST':
    #     form = courseratingForm(request.POST)
    #     if form.is_valid():
    #         ccd=request.POST.get('ccd')
    #         # form.save()
    #         courseratings = ratingcourse(course_code='19SE2112C',studentusername=susername,rating=form.data['rating'],remarks=form.data['remarks'])
    #         courseratings.save()
    #         print(form.data['rating'],form.data['remarks'])
            
            
    #         return HttpResponse("hy")
    # else:
    #     form = courseratingForm()
    # return render(request,'html/courserating.html',{'form':form,'susername':susername})


def updatescores(request,sname,ccd):
    fusername=request.session['fusername']
    csp = courseperformance.objects.all()
    studentregcourses = studentregisteredcourses.objects.filter(course_code=ccd)
    studs = student.objects.all()

    msg=None
    flag=courseperformance.objects.filter(susername=sname,coursecode=ccd)

    if flag:
        msg = "Already Updated"
    else:
        if request.method == 'POST':
            scorea=request.POST.get('score')
            update_scores = courseperformance(susername=sname,coursecode=ccd,facultyusername=fusername,score=scorea)
            update_scores.save()
            msg="Updated Succesfully"


    return redirect(updated,ccd=ccd,msg=msg)


def updated(request,ccd,msg):
    fusername=request.session['fusername']
    csp = courseperformance.objects.all()
    studentregcourses = studentregisteredcourses.objects.filter(course_code=ccd)
    studs = student.objects.all()
    return render(request,'html/registeredstudentsok.html',{'fusername':fusername,'studentregcourses':studentregcourses,'studs':studs,'ccd':ccd,'csp':csp,'msg':msg})


def registeredstudents(request,ccd):
    susername=request.session['susername']
    fusername=request.session['fusername']
    studentregcourses = studentregisteredcourses.objects.filter(course_code=ccd)
    studs = student.objects.all()
    return render(request,'html/registeredstudents.html',{'fusername':fusername,'studentregcourses':studentregcourses,'studs':studs,'ccd':ccd})

def mycourses(request):
    susername=request.session['susername']
    students = studentregisteredcourses.objects.filter(susername=susername)
    facallocation = facultycourseallocation.objects.all()
    csp = courseperformance.objects.filter(susername=susername)
    return render(request,'html/myregisteredcourses.html',{'students':students,'susername':susername,'facallocation':facallocation,'csp':csp})


def adminlog(request): 
    if request.method == 'POST':
        ausername =request.POST["auname"]
        apassword = request.POST["apwd"]
        flag = adminlogin.objects.filter(Q(username__iexact=ausername) & Q(password__iexact=apassword))
        if flag:
            request.session['ausername'] = ausername
            #return redirect('ownerhome')
            return render(request,'html/adminhomepage.html',{'ausername':ausername})
        else:
            return HttpResponse("Login Invalid")
    else:
        return render(request,'html/adminlogin.html')

def admin(request):
    return render(request,"admin")

def facultyreg(request):
    ausername=request.session['ausername']
    facultyreg = faculty.objects.all()
    if request.method == 'POST':
        form = facultyregisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Faculty added successfully"
            return render(request,'html/facultyregok.html',{'ausername':ausername,'msg':msg,'facultyreg':facultyreg})
    else:
        form = facultyregisterForm()
    return render(request,'html/addfaculty.html',{'form':form,'ausername':ausername,'facultyreg':facultyreg})


def addcourse(request):
    ausername=request.session['ausername']
    Courses = courses.objects.all()
    if request.method == 'POST':
        form = addcourseForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Course added successfully"
            return render(request,'html/courseaddedok.html',{'Courses':Courses,'ausername':ausername})
    else:
        form = addcourseForm()
    return render(request,'html/addcourse.html',{'form':form,'Courses':Courses,'ausername':ausername})

def studentreg(request):
    ausername=request.session['ausername']
    studentreg = student.objects.all()
    if request.method == 'POST':
        form = studentregisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg="student added successfully"
            return render(request,'html/studentregok.html',{'ausername':ausername,'msg':msg,'studentreg':studentreg})
    else:
        form = studentregisterForm()
    return render(request,'html/addstudent.html',{'form':form,'ausername':ausername,'studentreg':studentreg})

def addquiz(request):
    ausername=request.session['ausername']
    if request.method == 'POST':
        form = addtestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'html/ok.html')
    else:
        form = addtestForm()
    return render(request,'html/addtest.html',{'form':form,'ausername':ausername})


def facultylog(request): 
    if request.method == 'POST':
        fusername =request.POST["funame"]
        fpassword = request.POST["fpwd"]
        flag = faculty.objects.filter(Q(username__iexact=fusername) & Q(password__iexact=fpassword))
        if flag:
            request.session['fusername'] = fusername
            #return redirect('ownerhome')
            return render(request,'html/facultyhome.html',{'fusername':fusername})
        else:
            return HttpResponse("Login Invalid")
    else:
        return render(request,'html/facultylogin.html')

def studentlog(request): 
    if request.method == 'POST':
        susername = request.POST["suname"]
        spassword = request.POST["spwd"]
        flag = student.objects.filter(Q(username__iexact=susername) & Q(password__iexact=spassword))
        if flag:
            request.session['susername'] = susername
            #return redirect('ownerhome')
            return render(request,'html/studenthome.html',{'susername':susername})
        else:
            return HttpResponse("Login Invalid")
    else:
        return render(request,'html/studentlogin.html')

# def get_quiz(request):
#     try:
#         question_objs=Question.objects.all()
#         if request.GET.get('category'):
#             question_objs=question_objs.filter(category__category_name__icontains=request.GET.get('category'))
#         question_objs=list(question_objs)

#         data=[]
#         random.shuffle((question_objs))
#         print(question_objs)

#         for question_obj in question_objs:
#             data.append({
#                   "uid":question_obj.uid,
#                   "category": question_obj.category.category_name,
#                   "question":question_obj.question,
#                   "marks":question_obj.marks,
#                   "answers":question_obj.get_answers()


#                 })
#         payload={'status':True ,'data':data}

#         return JsonResponse(payload)


#     except Exception as e:
#         print(e)
#     return HttpResponse("Something went wrong")

# def homeq(request):
#     context={'categories' : Category.objects.all()}
#     if request.GET.get('category'):
#         return redirect(f"/quiz/?category={request.GET.get('category')}")
#     return render(request,"html/homeq.html",context)

# def quiz(request):
#     context={'category' : request.GET.get('category')}
#     return render(request,"html/quiz.html",context)

def studenthome(request):
    susername=request.session['susername']
    return render(request, "html/studenthome.html",{'susername':susername})

def facultyhome(request):
    fusername=request.session['fusername']
    return render(request, "html/facultyhome.html",{'fusername':fusername})