from django.db import models
from django.urls import reverse


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id', 'url', )

    def get_absolute_url(self):
        return reverse('bookmark:bookmark_detail', args=(self.url,))

