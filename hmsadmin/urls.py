from django.urls import path
from . import views
urlpatterns=[

    path('login/',views.fnLogin,name="admindashboard"),
    path('doctor/',views.Doctor,name='doctor'),
    path('header',views.Header),
    path('adddoctor/',views.fnadddoctor,name='adddoctor'),
    path('doctoradd/',views.adddoctorfn,name='doctoradd'),
    path('department/',views.Department,name='department'),
    path('staff/',views.fnstaff,name='staff'),
    path('addstaff/',views.fnaddstaff,name='addstaff'),
    path('staffadd/',views.fnstaffadd,name='staffadd'),
    path('staffcat/',views.fnstaffcat,name='staffcat'),
    path('addstaffcat/',views.fnaddstaffcat,name='addstaffcat'),
    path('deletecat/<cat_id>',views.fndeletecat,name="deletecat"),
    path('adddepartment/',views.Adddepartment,name='adddepartment'),
    path('contactqueries/',views.Contactqueries,name='queries'),
    path('opschedule/',views.Opschedule,name='schedule'),
    path('logout/',views.fnlogout,name="logout"),
    path('<dep_id>',views.fndelete,name="delete"),
    path('update/<upd_id>',views.Adddepartment,name="updatedep"),
     path('deletedoc/<docid>',views.fndeletedoc,name="deletedoc"),
    path('deletequery/<query_id>',views.fndeletequery,name="deletequery")
]