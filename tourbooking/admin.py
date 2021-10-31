from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'created_on', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'created_on')
    summernote_fields = ('description')
