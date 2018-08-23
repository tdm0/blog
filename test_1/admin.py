from django.contrib import admin

# Register your models here.

from .models import Question,text_base


admin.site.register(Question,erbose_name_plural='自带控件演示')

admin.site.register(text_base,erbose_name_plural='文本仓库')