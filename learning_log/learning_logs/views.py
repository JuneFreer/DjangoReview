from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required #导入了函数login_required()，将它作为装饰器@login_required用于视图函数topics(),让Python在运行topics()的代码前先运行login_required()的代码

from .models import Topic, Entry
from .forms import TopicForm, EntryForm # 引入模块forms.py中的TopicForm, EntryForm模型/类

# Create your views here.
def index(request): # request是用户输入的URL请求对象
    """学习笔记的主页homepage"""
    return render(request, 'learning_logs/index.html') # arg1: user's URL request, arg2: 一个可用于创建网页的模板template
    # 模板template定义了网页的结构

@login_required
#login_required()的代码检查用户是否已登录，仅当用户已登录时，Django才运行topics() 的代码。如果用户未登录，就重定向到登录页面
def topics(request):
    """显示所有的主题 topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # Topic是一个Model子类，objects.order_by()是这个类中的方法
    #用户登录后，request对象将有一个user属性，这个属性存储了有关该用户的信息.Topic.objects.filter(owner=request.user)让Django只从数据库中获取owner属性为当前用户的 Topic对象
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id): # 函数topic()捕获用户输入的URL中topic_id的值，并将其存储到形参topic_id中
    """显示单个主题topic及其所有的条目"""
    topic = Topic.objects.get(id=topic_id) # 我们使用get()来获取指定id的主题
    entries = topic.entry_set.order_by('-date_added')
    # 获取与该主题(topic)相关联的条目entries, 是先执行了上面那条语句，有了具体的topic，才能执行这一句
    context = {'topic': topic, 'entries': entries} # 将主题和条目都存储在字典context中
    return render(request, 'learning_logs/topic.html', context) # 再将这个字典context传给render(), 从而传给模板topic.html

@login_required
def new_topic(request):
    """添加新主题new topic"""
    if request.method != 'POST': # 情形1:用户刚进入new_topic网页(在这种情况下，它应显示一个空表单)
        # 未提交数据:创建一个新表单
        form = TopicForm() # new一个空表单对象
    else:                        # 情形2:对提交的表单数据进行处理，并将用户重定向到网页topics
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)    #使用用户输入的数据(它们存储在request.POST中)创建一个TopicForm实例,这样对象form将包含 用户提交的信息
        if form.is_valid(): #函数is_valid() 核实用户填写了所有必不可少的字段(表单字段默认都是必不可少的)，且输入的数据与要求的字段类型一致
        #这种自动验证避免了我们去做大量的工作
            form.save()    #如果所有字段都有效，我们就可调用save(),将表单中的数据写入数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            #使用reverse()获取页面topics的URL，并将其传递给HttpResponseRedirect(),后者将用户的浏览器重定向到页面topics

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):  #形参 topic_id，用于存储从URL中获得的值
    """在特定的主题topic中添加新条目new entry"""
    topic = Topic.objects.get(id=topic_id)    #从数据库中获取特定主题topic

    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST) #对用户输入表单的数据进行处理：创建一个EntryForm实例，使用request对象中的POST数据来填充它
        if form.is_valid():  #检查表单是否有效
            new_entry = form.save(commit=False) #让Django创建一个新的条目对象，并将其存储到new_entry中，但不将它保存到数据库中(实参commit=False)
            new_entry.topic = topic  #我们将new_entry的属性topic设置为在new_entry()函数开头从数据库中获取的主题topic
        new_entry.save()  #将新条目对象保存到数据库, 并将其与正确的主题topic相关联
        return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
        #调用reverse()时，需要提供两个实参: 1.要根据它来生成URL的URL模式的名称name='topic'; 2.列表args，其中包含要包含在URL中的所有实参

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """编辑既有条目edit existing entry"""
    #获取用户要修改的条目对象，以及与该条目相关联的主题
    entry = Entry.objects.get(id=entry_id) #通过entry_id从数据库表Entry中获取特定条目
    topic = entry.topic #通过entry的topic属性，获取entry所属的特定主题

    if request.method != 'POST':
        # 初次请求，使用当前条目(instance=entry)填充表单
        form = EntryForm(instance=entry)  #使用实参instance=entry创建一个 EntryForm实例。这个实参让Django创建一个表单，并使用既有条目对象中的信息填充它。 用户将看到既有的数据，并能够编辑它们。
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id])) #重 定向到显示条目所属主题的页面

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
