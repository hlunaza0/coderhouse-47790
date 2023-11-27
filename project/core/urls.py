
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
     path("core/" , views.home , name="index"), 
    
]
