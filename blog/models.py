from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class advertise(models.Model):
        district=models.CharField(max_length=100)
        category=models.IntegerField()
        img=models.ImageField(upload_to='pics')

class bidding1(models.Model):
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})