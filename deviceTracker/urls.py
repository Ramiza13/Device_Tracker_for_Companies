"""
URL configuration for deviceTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from deviceTracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about-us/', views.aboutUs),
    path('company_employees/', views.CompanyEmployee, name="company_employeed"),
    path('give_device/', views.DeviceHandout, name="device_handout"),
    path('device_handin/', views.DeviceHandin, name="device_handin"),
    path('see_info/', views.SeeInfo, name="see_information"),
]
