from django.contrib import admin

# Register your models here.

from .models import text_base

admin.site.register(text_base,erbose_name_plural='文本仓库')