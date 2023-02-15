
from distutils.command.upload import upload
from django.db import models 
#from django.contrib.auth import AbstractUser
#class User(AbstractUser):
 #   avatar = models.ImageField(upload_to='/uploads/%Y/%m')
# Create your models here.
class department(models.Model):
    department_id= models.AutoField(primary_key= True, null= False, unique=True)
    department_name= models.CharField(max_length= 100, null= False, unique= True )
    department_addr= models.CharField(max_length= 100, null= False)
    created_date_dp= models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return f'{self.department_id}, {self.department_name}, {self.department_addr} {self.created_date_dp}'
# Create your models here.
