from django.urls import path
from . import views


#urls conf
urlpatterns = [
    path('hello/', views.say_hello)
]