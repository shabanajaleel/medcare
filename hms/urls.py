from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.Home,name="home"),
    path('homehead',views.Homehead),
    path('department/<depid>',views.fndepart,name='department'),
    path('contact/',views.fnqueries,name="contact"),
    
]