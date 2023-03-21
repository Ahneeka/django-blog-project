import datetime

from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')

    def _str_(self):
        date = self.created_at
        ca = datetime.fromisoformat(str(date))
        date = ca.strftime('%y-%m-%d %H:%M:%s')
        string = f"""{self.title} -- {date}"""
        return string

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
