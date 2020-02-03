from django import forms

from .models import Topic, Entry #创建表单所需的数据模型data model

class TopicForm(forms.ModelForm): # 定义了一个名为TopicForm 的类，它继承了forms.ModelForm
    class Meta:    # 最简单的ModelForm版本只包含一个内嵌的Meta类
        model = Topic    # 它告诉Django根据哪个模型创建表单
        fields = ['text']    # 以 及在表单中包含哪些字段
        labels = {'text': ''}    # 让Django不要为字段text生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry    #EntryForm表单基于的模型
        fields = ['text']    #在表单中包含哪些字段
        labels = {'text': ''}    #给字段'text'指定了一个空标签
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}    #将文本区域Textarea的宽度设置为80 3 列，而不是默认的40列
