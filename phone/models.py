from django.db import models
from django.urls import reverse


# Create your models here.

class Phone(models.Model):
    name = models.CharField('NAME', max_length=50, blank=True)
    phonenum = models.CharField('PHONENUM', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', 'phonenum',)

    def get_absolute_url(self):
        return reverse('phone:phone_detail', args=(self.name,))
