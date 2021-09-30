from django.urls import path
from.import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('sags/', views.sags, name="sags"),
    path('foot/', views.foot, name="foot"),
    path('chess/', views.chess, name="chess"),
    path('esport/', views.esport, name="esport"),
    path('ehlel/', views.ehlel, name="ehlel"),
  


    

    path('', views.base, name='home'),
]
