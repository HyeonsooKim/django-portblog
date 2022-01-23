from django.shortcuts import render
from .models import Project
# 내가 만든 사이트에 필요한 기능을 정의하는 곳
# Create your views here.

def project_index(request):
    projects = Project.objects.all().order_by('-created_at')
    context = {'projects': projects}
    return render(request, 'project/project_index.html', context)



