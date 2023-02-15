from django.contrib import admin
from .models import employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['employee_id','department_id','employee_name', 'date_of_birth','employee_addr','employee_type','create_date', 'updated_date','avatar', 'cv' ]
    search_fields= ['employee_id', 'employee_name', 'department_id']
    list_filter=['employee_id', 'employee_name', 'department_id']
admin.site.register(employee, EmployeeAdmin)
# Register your models here.

# Register your models here.
