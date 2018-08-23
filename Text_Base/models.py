from django.db import models

# Create your models here.

class text_base(models.Model):
    Text_Title = models.CharField(max_length=100,default="无",verbose_name="文章标题",)
    Text_Text = models.TextField(default="可输入很长的文本",verbose_name="文章正文")
    Text_Demo = models.TextField(default="可输入很长的文本",verbose_name="演示代码",null=True,blank=True)
    Text_Image = models.ImageField(upload_to='File_home/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,default="无",verbose_name="上传图片",null=True,blank=True)
    Text_File = models.FileField(upload_to='File_home/%Y/%m/%d/',default="没有上传文件。",verbose_name="上传文件",null=True,blank=True)
    Text_ADD_DateTime = models.DateTimeField(auto_now=True,verbose_name="添加日期")

    class Meta:
        verbose_name='文本管理'
        verbose_name_plural='文本列表'