# Generated by Django 2.0.6 on 2018-08-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='text_base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text_Title', models.CharField(default='无', max_length=100, verbose_name='文章标题')),
                ('Text_Text', models.TextField(default='可输入很长的文本', verbose_name='文章正文')),
                ('Text_Demo', models.TextField(blank=True, default='可输入很长的文本', null=True, verbose_name='演示代码')),
                ('Text_Image', models.ImageField(blank=True, default='无', null=True, upload_to='File_home/%Y/%m/%d/', verbose_name='上传图片')),
                ('Text_File', models.FileField(blank=True, default='没有上传文件。', null=True, upload_to='File_home/%Y/%m/%d/', verbose_name='上传文件')),
                ('Text_ADD_DateTime', models.DateTimeField(auto_now=True, verbose_name='添加日期')),
            ],
            options={
                'verbose_name': '文本管理',
                'verbose_name_plural': '文本列表',
            },
        ),
    ]
