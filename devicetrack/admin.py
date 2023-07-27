from django.contrib import admin
from devicetrack.models import CompanyEmployees
from devicetrack.models import deviceGive
from devicetrack.models import deviceReturn

# Register your models here.


class Employee(admin.ModelAdmin):
    list_display=('employeeName','companyName','contact','email')

admin.site.register(CompanyEmployees, Employee)

class giveDevice(admin.ModelAdmin):
    list_display=('employeeName','deviceName','checkoutDate','deviceCondition1')

admin.site.register(deviceGive, giveDevice)

class returnDevice(admin.ModelAdmin):
    list_display=('employeeName','deviceName','returnDate','deviceCondition2')

admin.site.register(deviceReturn, returnDevice)

