from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Profile(models.Model):
        user=models.OneToOneField(User,on_delete=models.CASCADE)
        image=models.ImageField(default='default.png',upload_to='profile_pics')
        banner=models.ImageField(default='default.png',upload_to='profile_pics')
        bid=models.IntegerField(default=0)
        def __str__(self):
                return self.user.username+" Profile"
                
        def save(self, *args, **kwargs):
                super(Profile, self).save(*args, **kwargs)
                img=Image.open(self.image.path)
                if img.height>300 or img.width>300:
                        output_size=(300,300)
                        img.thumbnail(output_size)
                        img.save(self.image.path)

class chek(models.Model):
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)

