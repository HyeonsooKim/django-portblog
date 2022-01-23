from django.contrib import admin
from .models import Project
# 장고에서 제공해주는 관리자 페이지 설정
# Register your models here.

# 내가 만든 DB를 가져와 어드민 사이트에서 등록을 하겠다
admin.site.register(Project)

