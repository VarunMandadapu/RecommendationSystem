from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.mainhome,name="mainhome"),
    path("home/",views.home,name="home"),
    path("studentlog/",views.studentlog,name="studentlog"),
    path("facultylog/",views.facultylog,name="facultylog"),
    path("viewallocated/",views.viewallocated,name="viewallocated"),
    path("studentdata/",views.studentdata,name="studentdata"),
    path("adminlog/",views.adminlog,name="adminlog"),
    path('admin/', admin.site.urls),
    path("home/",views.home,name="home"),
    path("adminhome/",views.adminhome,name="adminhome"),
    path("facultyreg/",views.facultyreg,name="facultyreg"),
    path("studentreg/",views.studentreg,name="studentreg"),
    # path("api/get-quiz/",views.get_quiz,name="get_quiz"),
    # path("quiz/",views.quiz,name="quiz"),
    path("displayquiz/",views.displayquiz,name="displayquiz"),
    path("savequiz/",views.savequiz,name="savequiz"),
    path("studenthome/",views.studenthome,name="studenthome"),
    path("registeredcourses/<cid>",views.registercourses,name="registercourses"),

    path("updatescores/<sname>/<ccd>",views.updatescores,name="updatescores"),
    path("mycourses",views.mycourses,name="mycourses"),
    path("facultyhome/",views.facultyhome,name="facultyhome"),
    path("addquiz/",views.addquiz,name="addquiz"),
    path("registeredstudents/<ccd>",views.registeredstudents,name="registeredstudents"),
    path("courseallocation/",views.courseallocation,name="courseallocation"),
    path("updated/<ccd>/<msg>",views.updated,name="updated"),
    path("courserating/<ccd>",views.courserating,name="courserating"),
    path("addcourse/",views.addcourse,name="addcourse"),
    path("viewcourses/",views.viewcourses,name="viewcourses"),


    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)