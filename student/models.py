from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    studentnum = models.CharField('STUDENTNUM', max_length=10, blank=False)
    name = models.CharField('NAME', max_length=100, blank=False)
    department = models.CharField('DEPARTMENT', max_length=20, blank=False)
    tel = models.CharField('MOBILE', max_length=50, blank=False)
    email = models.EmailField('EMAIL', max_length=50, blank=True)
    address = models.CharField('ADDRESS', max_length=50, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.studentnum

    class Meta:
        ordering = ('tel', 'name',)

    def get_absolute_url(self):
        return reverse('student:student_detail', args=(self.name,))
