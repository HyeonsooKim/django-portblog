# Generated by Django 4.0.1 on 2022-01-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='타이틀')),
                ('description', models.TextField(verbose_name='프로젝트 내용')),
                ('tech', models.CharField(max_length=100, verbose_name='사용 기술')),
                ('image', models.ImageField(blank=True, null=True, upload_to='project', verbose_name='프로젝트 이미지')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
