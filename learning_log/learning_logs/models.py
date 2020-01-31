# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class Topic(models.Model):    #创建了一个名为Topic的类，它继承了models模块中的Model类
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #on_delete=models.CASCADE意思是当删除一个Topic时，Django会把与之相关的外键entries都删除
    #Note on_delete=models.CASCADE means that on deleting Topic object, Django deletes the objects containing the ForeignKey(entries)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) > 50:
            stringRepresent = self.text[:50] + "..."
        else:
            stringRepresent = self.text
        return stringRepresent
