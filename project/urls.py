#브라우저의 주소창에 넣는 주소를 정의해주는 곳

from django.urls import path
from . import views

"""
앱 자체의 주소 설정을 해줬으니 앱 안에서 메인화면과 디테일 화면의 세부 주소 형식을 설정해줘야함

메인화면은 주소창에 /(슬래쉬)로 설정을 할 것이기 때문에 비워두고 name은 index로 설정해둠

app_name은 다른 앱과의 차별화를 두기 위해 지정함

project의 메인화면은 index 이름이고, blog 앱의 메인 화면도 index 이름을 가지면 헷갈리게 됨

그래서 별도의 이름을 지정해줌
"""
app_name = 'project'
urlpatterns = [
    path('', views.project_index, name='index'),
    path('detail/<int:id>', views.project_detail, name='detail'),
]