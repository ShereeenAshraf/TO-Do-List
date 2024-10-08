from django.db import models
from django.contrib.auth.models import User # for django authentication

# Create your models here.
class Task(models.Model):
    # one to many  relationship  one user has many iteams 
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
    