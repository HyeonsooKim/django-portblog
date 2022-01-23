from django.db import models

#데이터를 저장하는 모델명을 정의
# 내가 만든 포폴 데이터들을 데이터베이스에 저장하고 그것을 웹사이트에 뿌려주는 역할
# Create your models here.

class Project(models.Model):
    title = models.CharField("타이틀", max_length=200)
    description = models.TextField("프로젝트 내용")
    tech = models.CharField("사용 기술", max_length=100)
    image = models.ImageField("프로젝트 이미지", blank=True, null=True, upload_to='project')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title