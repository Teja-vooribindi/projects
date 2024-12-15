
from django.db import models

class EmployeeLogin(models.Model):
    user_id = models.AutoField(primary_key=True)  
    login_id = models.CharField(max_length=100, unique=True) 
    password = models.CharField(max_length=255) 
    employee_name = models.CharField(max_length=100) 

    def __str__(self):
        return self.login_id
