from django.db import models

# Create your models here.


class CompanyEmployees(models.Model):
    employeeName=models.CharField('Employee Name', max_length=50)
    companyName=models.CharField(max_length=50, null=True)
    contact=models.CharField(max_length=25, null=True) #widget=AdminDateWidget()
    email=models.EmailField('Email Address', max_length=254)  #(default=date.today)

    def __str__(self):
        return self.employeeName


class deviceGive(models.Model):
    #employeeName=models.ForeignKey(CompanyEmployees, blank=True, null=True, on_delete=models.CASCADE)
    employeeName=models.CharField('Employee Name', max_length=50, null=True)
    deviceName=models.CharField('Device Name', max_length=50)
    checkoutDate=models.DateField('Check-out Date', null=True) #, auto_now_add=True, null=True   #widget=AdminDateWidget()
    #returnDate=models.DateField('Return Date', null=True)  #(default=date.today) 
    deviceCondition1=models.TextField('Condition of Device during handing out', null=True)
    #deviceCondition2=models.TextField('Condition of Device during handing in')

    #def __str__(self):
     #   return self.employeeName

class deviceReturn(models.Model):
    #employeeName=models.ForeignKey(CompanyEmployees, blank=True, null=True, on_delete=models.CASCADE)
    employeeName=models.CharField('Employee Name', max_length=50, null=True)
    deviceName=models.CharField('Device Name', max_length=50)
    #checkoutDate=models.DateField('Check-out Date', null=True) #, auto_now_add=True, null=True   #widget=AdminDateWidget()
    returnDate=models.DateField('Return Date', null=True)  #(default=date.today) 
    #deviceCondition1=models.TextField('Condition of Device during handing out')
    deviceCondition2=models.TextField('Condition of Device during handing in', null=True)
    
    #def __str__(self):
     #   return self.employeeName