from django.db import models
from django.contrib import admin
from datetime import datetime    
import uuid
import random

class adminlogin(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False,unique=True)
    password = models.CharField(max_length=100, blank=False)
    class Meta:
        db_table = "admin_table"


class student(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=100,blank=False)
    fullname = models.CharField(max_length=100,blank=False)
    gender_choices = ( ('Male','MALE') , ('Female','FEMALE') )        
    gender = models.CharField(max_length=100,blank=False,choices=gender_choices)
    dob=models.CharField(max_length=100,blank=False)
    department=models.CharField(max_length=100,blank=False)
    program=models.CharField(max_length=100,blank=False)
    cgpa=models.CharField(max_length=100,blank=False)
    backlogs=models.CharField(max_length=100,blank=False)
    username = models.CharField(max_length=100, blank=False,unique=True)
    email = models.EmailField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100, blank=False)
    mobileno = models.CharField(max_length=100,blank=False,unique=True)
    location = models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = "student_table"

    def __str__(self) -> str:
        return f"{self.fullname,self.gender,self.dob,self.program,self.cgpa,self.backlogs,self.username,self.email,self.mobileno,self.location}"
   

class faculty(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100,blank=False)
    gender_choices = ( ('Male','MALE') , ('Female','FEMALE') )        
    gender = models.CharField(max_length=100,blank=False,choices=gender_choices)
    dob=models.CharField(max_length=100,blank=False)
    department=models.CharField(max_length=100,blank=False)
    qualification=models.CharField(max_length=100,blank=False)
    experience=models.CharField(max_length=100,blank=False)
    salary=models.CharField(max_length=100,blank=False)
    username = models.CharField(max_length=100, blank=False,unique=True)
    email = models.EmailField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100, blank=False)
    mobileno = models.CharField(max_length=100,unique=True,blank=False)
    location = models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = "faculty_table"


class questionbank(models.Model):
    question_choices = ( ('EXTROVERTED','EXTROVERTED') , ('INTROVERTED','INTROVERTED'), ('SENSING','SENSING') , ('INTUITIVE','INTUITIVE') , ('THINKING','THINKING') , ('FEELING','FEELING') , ('JUDGING','JUDGING') , ('PROSPECTING','PROSPECTING') )        
    category = models.CharField(max_length=100,blank=False,choices=question_choices)
    question_id = models.AutoField(primary_key=True)
    question_rid=models.CharField(blank=False,max_length=100)
    question=models.CharField(max_length=500,blank=False,unique=True)
    answer1=models.CharField(max_length=100,blank=False)
    answer2=models.CharField(max_length=100,blank=False)
    answer3=models.CharField(max_length=100,blank=False)
    answer4=models.CharField(max_length=100,blank=False)

    # answer_choices = ( ('answer1','answer1') , ('answer2','answer2') , ('answer3','answer3') , ('answer4','answer4'))

    correctanswer = models.CharField(max_length=100,blank=False,default="NA")




    class Meta:
        db_table = "questionbank_table"

    


class courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    category_choices = ( ('CORE','CORE') , ('PROFESSIONAL','PROFESSIONAL ELECTIVE') )        
    category = models.CharField(max_length=100,blank=False,choices=category_choices)
    specialization_choices = ( ('SECURITY AND FORENSICS','SECURITY AND FORENSICS') , ('NETWORKING','NETWORKING') , ('APP DEVELOPMENT','APP DEVELOPMENT') ) 
    specialization = models.CharField(max_length=100,blank=False,choices=specialization_choices)
    course_code=models.CharField(max_length=100,blank=False,unique=True)
    course_title=models.CharField(max_length=100,blank=False)
    description=models.CharField(max_length=100,blank=False)
    courselink=models.CharField(max_length=100,blank=False)
    
    class Meta:
        db_table = "courses_table"

    def __str__(self) -> str:
        return f"{self.category,self.specialization,self.course_code,self.course_title,self.description}"


class ratingcourse(models.Model):
    courserating_id = models.AutoField(primary_key=True)
    course_code=models.CharField(max_length=100,blank=False)
    studentusername=models.CharField(max_length=100,blank=False)
    rating_choices = ( ('1','1') , ('2','2') , ('3','3') , ('4','4') , ('5','5') )       
    rating=models.CharField(max_length=100,blank=False,choices=rating_choices)
    remarks=models.CharField(max_length=1000,blank=True)
    ratingtime = models.DateTimeField(default=datetime.now, blank=True)
     
    class Meta:
        db_table = "courserating_table"

class quiz_result(models.Model):
    aid = models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False)
    label=models.CharField(max_length=100,blank=False)
    specialization=models.CharField(max_length=100,blank=False)
    timestamp=models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = "quizresult_table"

class facultycourseallocation(models.Model):
    aid = models.AutoField(primary_key=True)
    fusername=models.CharField(max_length=100,blank=False)
    course_code=models.CharField(max_length=100,blank=False)
    # course_code=models.ForeignKey(courses,related_name='coursecode', on_delete=models.CASCADE)
    course_title=models.CharField(max_length=200,blank=False)
    
    class Meta:
        db_table = "facultycourseallocation_table"

class studentregisteredcourses(models.Model):
    regid = models.AutoField(primary_key=True)
    susername=models.CharField(max_length=100,blank=False)
    course_id = models.CharField(max_length=100,blank=False)
    course_code=models.CharField(max_length=100,blank=False)
    course_title=models.CharField(max_length=100,blank=False)
    timestamp=models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = "studentregistered_table"

    def __str__(self) -> str:
        return f"{self.regid,self.susername,self.course_id,self.course_code,self.course_title,self.timestamp}"

class courseperformance(models.Model):
    updateid = models.AutoField(primary_key=True)
    susername = models.CharField(max_length=100,blank=False)
    coursecode = models.CharField(max_length=100,blank=False)
    facultyusername = models.CharField(max_length=100,blank=False)
    score = models.CharField(max_length=100,blank=False)
    Time = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = "courseperformance_table"



class temp(models.Model):
    sno =  models.AutoField(primary_key=True)
    sname = models.CharField(max_length=100,blank=False)
    a1 = models.CharField(max_length=100,blank=False)
    a2 = models.CharField(max_length=100,blank=False)
    a3 = models.CharField(max_length=100,blank=False)
    a4 = models.CharField(max_length=100,blank=False)
    b1 = models.CharField(max_length=100,blank=False)
    b2 = models.CharField(max_length=100,blank=False)
    b3 = models.CharField(max_length=100,blank=False)
    b4 = models.CharField(max_length=100,blank=False)
    c1 = models.CharField(max_length=100,blank=False)
    c2 = models.CharField(max_length=100,blank=False)
    c3 = models.CharField(max_length=100,blank=False)
    c4 = models.CharField(max_length=100,blank=False)
    d1 = models.CharField(max_length=100,blank=False)
    d2 = models.CharField(max_length=100,blank=False)
    d3 = models.CharField(max_length=100,blank=False)
    d4 = models.CharField(max_length=100,blank=False)
    label = models.CharField(max_length=100,blank=False)
    specialization = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "temp_table"


    
    




