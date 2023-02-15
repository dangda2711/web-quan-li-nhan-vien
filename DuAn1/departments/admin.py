from django.contrib import admin
from .models import department

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display= ['department_id','department_name','department_addr', 'created_date_dp' ]
    search_fields= ['department_id', 'department_name']
    list_filter=['department_id', 'department_name']
admin.site.register(department, DepartmentAdmin)
# Register your models here.
