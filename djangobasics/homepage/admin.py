from django.contrib import admin
from .models import ResumeModel
# Register your models here.

# admin.site.register(ResumeModel)
@admin.register(ResumeModel)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id','BookName','AuthorName','file']