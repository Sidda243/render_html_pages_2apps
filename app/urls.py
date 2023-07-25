app_name='nothing'
from django.urls import path
from app.views import *

urlpatterns = [
    path('hii/',hii,name='hii'),
    path('hello/',hello,name='hello'),
]