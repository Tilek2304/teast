from django.contrib import admin
from django.utils.html import format_html
from .models import SubjectFile

@admin.register(SubjectFile)
class SubjectFileAdmin(admin.ModelAdmin):

    readonly_fields = ['img_out']
    list_display = ['name', 'subject', 'file', 'uploaded_at']
    list_filter = ['subject']
    search_fields = ('file',)
    @admin.display(description='Просмотр фотографии')
    def img_out(self,obj):
        return format_html(f'<img src="/media/{obj.image}" width="250" />')  
