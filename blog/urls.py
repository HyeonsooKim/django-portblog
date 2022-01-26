from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_index, name='index'),
    path('detail/<int:id>/', views.blog_detail, name='detail'),
    path('<category>/', views.blog_category, name='category'),
]