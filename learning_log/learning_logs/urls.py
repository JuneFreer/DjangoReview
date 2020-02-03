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
    path('topics/', views.topics, name='topics'),

    # 显示特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # 用于添加新主题new_topic的网页
    path('new_topic/', views.new_topic, name='new_topic'),

    # 用于添加新条目new_entry的页面. 请求的URL与这个模式匹配时，Django将请求URL和主题ID发送给函数new_entry()
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # 用于编辑条目edit entry的页面. 在URL(如http://localhost:8000/edit_entry/1/)中传递的ID存储在形参entry_id中
    # 这个URL模式,将与之匹配的请求发送给视图函数edit_entry()
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
