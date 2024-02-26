from django.db import models

# Create your models here.
class Contentitem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return self.title
    
class Item (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return self.title
    

class Colum (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='favicon/')    


    def __str__(self):
        return self.title