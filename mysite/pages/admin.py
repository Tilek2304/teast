from django.contrib import admin
from .models import SubjectFile

@admin.register(SubjectFile)
class SubjectFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'uploaded_at']
    list_filter = ['subject']
    search_fields = ('name',)  
