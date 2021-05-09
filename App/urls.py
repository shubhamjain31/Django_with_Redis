
from django.urls import path, include

from App.views import *

urlpatterns = [

    path('',home , name='home'),
    path('<int:id>',show , name='show'),
    
]