from django import forms
from .models import *

class adminregisterForm(forms.ModelForm):
  class Meta:
    model = adminlogin
    fields = "__all__"

class facultyregisterForm(forms.ModelForm):
  class Meta:
    model = faculty
    fields = "__all__"

class addcourseForm(forms.ModelForm):
  class Meta:
    model = courses
    fields = "__all__"

class courseAllocationForm(forms.ModelForm):
  class Meta:
    model = facultycourseallocation
    fields = "__all__"
   

class studentregisterForm(forms.ModelForm):
  class Meta:
    model = student
    fields = "__all__"

class addtestForm(forms.ModelForm):
  class Meta:
    model = questionbank
    fields = "__all__"
    exclude=['correctanswer']

class courseratingForm(forms.ModelForm):
  class Meta:
    model = ratingcourse
    fields = "__all__"
    exclude=['course_code','studentusername','ratingtime']


class quizForm(forms.ModelForm):
  class Meta:
    model = questionbank
    fields = "__all__"
    widgets = {'answer1': forms.RadioSelect,'answer2': forms.RadioSelect,'answer3': forms.RadioSelect,'answer4': forms.RadioSelect}
    exclude=['correctanswer','question']