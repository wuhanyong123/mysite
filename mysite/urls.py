"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app01 import views

#保存了路径和函数的对应关系
urlpatterns = [
    # url(r'^yimi/', yimi),
    # url(r'^xiaohei/', xiaohei),
    url(r'^login/', views.login),
    url(r'^user_list/', views.user_list),
    url(r'^add_user/', views.add_user),
    url(r'^delete_user/', views.delete_user),
    url(r'^edit_user/', views.edit_user),
]
