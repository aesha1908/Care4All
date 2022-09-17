from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("",views.index,name='home'),
   path("about",views.about,name='about'),
   path("work",views.work,name='work'),
   path("mission",views.mission,name='mission'),
   path("team",views.team,name='team'),
   path("state",views.state,name='state'),
   path("achieve",views.achieve,name='achieve'),
   path("donate",views.donate,name='donate'),
   path("job",views.job,name='job'),
   path("login",views.login,name='login'),
]
