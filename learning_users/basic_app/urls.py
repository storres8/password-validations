from django.urls import path, include
from basic_app import views


# global variable decloration for url template tagging must match the apps name
app_name= 'basic_app'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name='user_login'),
    path('user_special/', views.user_special, name='user_special')
]
