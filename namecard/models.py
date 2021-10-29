from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Namecard(models.Model):
    name = models.CharField('NAME', max_length=100, blank=False)
    tel = models.CharField('MOBILE', max_length=50, blank=False, unique=True)
    company = models.CharField('COMPANY', max_length=50, blank=True)
    email = models.EmailField('EMAIL', max_length=50, blank=True)
    group = models.CharField('Group', max_length=50, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    """
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    birth_dt = models.DateTimeField('BIRTH DATE', blank=True, auto_now=False)
    """

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('group', 'name',)

    def get_absolute_url(self):
        return reverse('namecard:namecard_detail', args=(self.name,))
