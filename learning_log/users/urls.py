"""为应用程序users定义URL模式"""

from django.urls import include, path
from django.contrib.auth import views as auth_views #导入了django.contrib.auth中的默认(内置)视图 LoginView

from . import views

#命名空间
app_name = 'users' # 让Django在users/urls.py中查找

urlpatterns = [
    # 登录页面 login page
    #如果你不愿意调用默认模板registration/login.html,你可以通过附加参数的形式传递template_name参数给你的URLconf中的as_view()方法.
    #'https://docs.djangoproject.com/zh-hans/3.0/topics/auth/default/#topic-authorization'
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # 注销/登出logout
    path('logout/', views.logout_view, name='logout'),

    # 注册页面 register page
    path('register/', views.register, name='register'),


]

# {'template_name': 'users/login.html'}
