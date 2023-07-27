from django.http import HttpResponse
from django.shortcuts import render,redirect
#from .forms import userForm
from devicetrack.models import CompanyEmployees
from devicetrack.models import deviceGive
from devicetrack.models import deviceReturn
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

def homePage(request):
    data={
        'title': 'Home Page New',
        'body_data': 'Homepage has started now'
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("<b>Welcome</b>")

def CompanyEmployee(request):
    #emp = CompanyEmployees.objects.all()

    n =  ''

    if request.method=='POST':
        name=request.POST.get('empName')
        companyName=request.POST.get('compname')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        en=CompanyEmployees(employeeName=name,companyName=companyName,contact=contact,email=email)
        en.save()
        n='Data Inserted'

    return render(request, "companyemployees.html",{'n':n})

def DeviceHandout(request):
    n =  ''

    if request.method=='POST':
        name=request.POST.get('empName')
        device=request.POST.get('device')
        checkoutDate=request.POST.get('checkoutDate')
        deviceSituation1=request.POST.get('deviceSituation')
        en=deviceGive(employeeName=name,deviceName=device,checkoutDate=checkoutDate,deviceCondition1=deviceSituation1)
        en.save()
        n='Data Inserted'

    return render(request, "givedevice.html",{'n':n})

def DeviceHandin(request):
    n =  ''

    if request.method=='POST':
        name=request.POST.get('empName')
        device=request.POST.get('device')
        returnDate=request.POST.get('returnDate')
        deviceSituation2=request.POST.get('deviceSituation')
        en=deviceReturn(employeeName=name,deviceName=device,returnDate=returnDate,deviceCondition2=deviceSituation2)
        en.save()
        n='Data Inserted'

    return render(request, "returndevice.html",{'n':n})


def SeeInfo(request):
    emp = CompanyEmployees.objects.all()
    give=deviceGive.objects.all()
    returned=deviceReturn.objects.all()

    
    n =  ''

    if request.method=='POST':
        name=request.POST.get('EmpName')
        company=request.POST.get('compname')
        

    data={
        'emp':emp,
        'give':give,
        'returned':returned
    }

    return render(request, "seeinformation.html",data)
