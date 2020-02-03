"""learning_log URL Configuration URLconf

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

"""To design URLs for an app, you create a Python module informally called a URLconf (URL configuration).
This module is pure Python code and is a mapping between URL path expressions to Python functions (your views)."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), # 包含admin后台的所有页面的URL
    #path('learning_logs/', include('learning_logs.urls')),
    # 包含App learning_logs中的所有页面的URL，具体在learning_logs/urls.py中
    # URL中必须包含'learning_logs/',因为这里的第一个参数包含了'learning_logs/', http://127.0.0.1:8000/learning_logs
    # 如果希望URL中不包含'learning_logs/'，这里第一个参数就必须为空 http://127.0.0.1:8000/
    path('', include('learning_logs.urls')),
    path('users/', include('users.urls')),
]
