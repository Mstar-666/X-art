from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='姓名')

    avatar = models.ImageField(verbose_name='头像')

    teacher_desc = models.TextField(verbose_name='教师简介')

    def __str__(self):
        return self.name

    class Meta:  # 定义数据库表和类的关系
        db_table = 't_teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name