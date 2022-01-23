#브라우저의 주소창에 넣는 주소를 정의해주는 곳

from django.urls import path
from . import views

app_name = 'project'
urlpatterns =[
    path('', views.project_index, name='index')
]