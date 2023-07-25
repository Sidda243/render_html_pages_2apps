app_name='nothing1'
from django.urls import path
from app1.views import *

urlpatterns = [
    path('my/',my,name='my'),
    path('my1/',my1,name='my1'),
]