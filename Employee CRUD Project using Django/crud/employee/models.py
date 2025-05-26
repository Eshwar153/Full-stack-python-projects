from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField()
    employee_contact = models.CharField(max_length=20)

    def __str__(self):
        return self.employee_name