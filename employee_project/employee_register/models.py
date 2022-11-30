from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    #gets the state representation of the class. In this
    #case we want the title to represent the class
    def __str__(self):
        return self.title

#remember to inherit from Model
class Employee(models.Model):
    fullname = models.CharField(max_length=100) 
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
