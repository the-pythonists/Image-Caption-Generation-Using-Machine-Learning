from django.db import models

# Create your models here.

class Register(models.Model):
    FirstName = models.CharField(max_length=50,default='',blank=True)
    LastName = models.CharField(max_length=50,default='',blank=True)
    Password = models.CharField(max_length=100,default='',blank=True)
    Email = models.EmailField(blank=True)
    SecurityQuestion = models.CharField(max_length=150,default='',blank=True)
    SecurityAnswer = models.CharField(max_length=500,default='',blank=True)
    
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
        ]
    Gender = models.CharField(max_length=1,default='',choices=GENDER_CHOICES)

    def __str__(self):
        return f'{self.FirstName} {self.LastName}'