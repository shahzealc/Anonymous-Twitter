from distutils.command.upload import upload
from django.db import models

class Tweet(models.Model):
    titlee = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    tag = models.CharField(max_length=20,default='education')
    image_post = models.ImageField(null=True,blank=True,upload_to="images/")
    creation_date = models.DateField()

    def __str__(self):  
            return self.titlee