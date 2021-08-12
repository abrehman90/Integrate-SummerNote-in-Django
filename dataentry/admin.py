from django.contrib import admin
from .models import *
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(user, PostAdmin)
