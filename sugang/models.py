# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from gwamok.models import Gwamok


# Create your models here.
class Sugang(models.Model):
    #gwamok = models.CharField('GWAMOK', max_length=15, blank=False)
    name = models.CharField('NAME', max_length=100, blank=False)
    professor = models.CharField('PROFESSOR', max_length=100, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    """
    semester = models.CharField('SEMESTER', max_length=10, blank=False)
    name = models.CharField('NAME', max_length=100, blank=False)
    professor = models.CharField('PROFESSOR', max_length=100, blank=False)
    day = models.CharField('DAY', max_length=50, blank=False)
    time = models.CharField('TIME', max_length=100, blank=False)
    classroom = models.CharField('CLASSROOM', max_length=100, blank=False)
    """
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name')

    def get_absolute_url(self):
        return reverse('sugang:sugang_detail', args=(self.name,))


    # 과목 테이블 / id 학기 과목명 담당교수 요일 시간 강의실 수강인원