"""定义learning_logs的URL模式"""

#from django.conf.urls import url
from django.urls import include, path
from . import views # 其中的句点让Python从当前的urls.py模块所在的文件夹中导入视图 views.py

app_name = 'learning_logs' # 必须在learning_logs/urls.py中加上app_name属性,否则会出错：'learning_logs' is not a registered namespace
# 变量urlpatterns是一个列表，包含可在应用程序learning_logs中请求的网页
urlpatterns = [
    # 主页 homepage: 'http://127.0.0.1:8000/' 
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index'), # arg1: regex, arg2: view function, arg3: URL name

    # 显示所有的主题 topics: 'http://127.0.0.1:8000/topics'
    path('topics/', views.topics, name='topics')
]
