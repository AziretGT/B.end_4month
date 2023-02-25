from django.urls import path 
from posts.views import hello, get_index, get_info, get_help

urlpatterns = [
path ("hello/", hello, name ="hello-view"),
path ("", get_index, name ="index-page"),
path ("info/",get_info, name ="endpoint-info"),
path ("help", get_help, name="get-help"),
]     