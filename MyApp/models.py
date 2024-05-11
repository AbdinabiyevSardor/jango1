from django.db import models

# Create your models here.

    

class Post(models.Model):
    image = models.ImageField(upload_to="Post/")
    full_name = models.CharField(max_length=250)
    

    
    def str(self):
        return self.full_name