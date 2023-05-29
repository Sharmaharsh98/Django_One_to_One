from django.db import models

# Create your models here.
class Ceo(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    salary = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.full_name}'

class Company(models.Model):
    ceo = models.OneToOneField(Ceo, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    company_domain = models.CharField(max_length=50)
    company_revenue = models.CharField(max_length=50)
    company_headoffice = models.CharField(max_length=50)