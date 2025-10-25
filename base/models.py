from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class employess(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class talks(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
class notifications(models.Model):
    From=models.CharField(max_length=150)
    to=models.CharField(max_length=150)
    message=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user
    


