from django.urls import path 
from posts.views import hello, get_index, get_about, get_contact

urlpatterns = [
path ("hello/", hello, name ="hello-view"),
path ("", get_index, name ="index-page"),
path ("about/",get_about, name ="endpoint-about"),
path ("contact/", get_contact, name="get-contact"),
]     