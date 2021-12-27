from django.urls import path
from . import views

urlpatterns=[
    path('dashbord/',views.fndashbord,name="dashbord"),
    path('dashheader/',views.fnheader,name="dashheader")

]