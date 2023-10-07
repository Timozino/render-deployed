from django.db import models
from cloudinary.models import CloudinaryField

class Library(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    course_image=CloudinaryField('course_image', null=True)
    #author_image=CloudinaryField('author_image', null=True)
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering=['title']
        
class AuthorImage(models.Model):
    title=models.CharField(max_length=100)
    author_image=CloudinaryField('author_image', null=True)
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering=['title']