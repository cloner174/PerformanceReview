from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='employees')
    
    def __str__(self):
        return self.user.username
    


class Question(models.Model):
    
    text = models.TextField()
    
    def __str__(self):
        return self.text
    


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    response = models.TextField()
    
    def __str__(self):
        return f"{self.employee} - {self.question}"
    
#cloner174