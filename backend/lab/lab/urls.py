from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='index'),
    path('question', question.as_view(), name='question'),
    path('add-question', add_question.as_view(), name='add_question'),
    path('tag', tag.as_view(), name='tag'),
    path('profile', profile.as_view(), name='profile'),
    path('login', login.as_view(), name='login'),
    path('signup', signup.as_view(), name='signup'),
]
