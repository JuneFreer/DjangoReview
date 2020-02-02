from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request): # request是用户输入的URL请求对象
    """学习笔记的主页homepage"""
    return render(request, 'learning_logs/index.html') # arg1: user's URL request, arg2: 一个可用于创建网页的模板template
    # 模板template定义了网页的结构

def topics(request):
    """显示所有的主题 topics"""
    topics = Topic.objects.order_by('date_added') # Topic是一个Model子类，objects.order_by()是这个类中的方法
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
