from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate #导入Django函数logout(), login(), authenticate()
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """注销用户logout"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index')) #重定向回主页

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save() #调用表单的方法save()，将用户名和密码的散列值保存到数据库中,方法save()返回新创建的用户对象
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            #如果用户名和密码无误，方法authenticate()将返回一个通过了身份验证的用户对象，而我们将其存储在authenticated_user 8 中
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
