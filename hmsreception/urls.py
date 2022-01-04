from django.urls import path
from . import views

urlpatterns=[
    path('recdashbord/',views.fnrecdash,name="recdashbord"),
    path('addappointment/',views.fnappointment,name="addappointment"),
    path('viewappointment/',views.fnviewappointment,name="viewappointment"),
    path('selectdoctor/',views.fnselectdr,name="selectdoctor"),
    path('selectday/',views.fnselectday,name="selectday"),
    path('viewdoctor/',views.fnviewdoctor,name="viewdoctor"),
   
    
]