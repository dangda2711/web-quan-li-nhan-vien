
from django.db import models 
from django.contrib.auth.models import AbstractUser
from departments.models import department
#class User(AbstractUser, models.Model):   
 #   avatar = models.ImageField(upload_to='uploads/%Y/%m')
# Create your models here.
class employee(models.Model):
    employee_id= models.AutoField(primary_key= True, null= False, unique=True)
    department_id= models.ForeignKey(department, on_delete=models.CASCADE )  #Khi mà xóa phòng ban toàn bộ nhân viên xóa theo
    employee_name= models.CharField(max_length=100, null= False, unique= True)
    date_of_birth= models.DateField()
    employee_addr= models.TextField( null= False, blank= True)
    employee_type= models.IntegerField(null= True)
    create_date= models.DateTimeField( auto_now_add=True)
    updated_date= models.DateTimeField( auto_now=True)
    avatar= models.ImageField(upload_to='images', null= False,default= None )
    cv= models.FileField(upload_to= 'files', null = False, default=None)
    active= models.BooleanField(default= True)

    def __str__(self):
        return f'{self.employee_id},{self.department_id}, {self.employee_name}, {self.date_of_birth}, {self.employee_addr},{self.employee_type},{self.create_date}, {self.updated_date},{self.avatar}, {self.active}  '
