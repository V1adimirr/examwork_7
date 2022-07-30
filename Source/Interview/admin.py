from django.contrib import admin

from Interview.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_at']
    list_filter = ['question']
    search_fields = ['created_at']
    readonly_fields = ['created_at']
    fields = ['question', 'created_at']


admin.site.register(Poll, PollAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['option', 'interview']
    list_filter = ['option']
    search_fields = ['interview']
    fields = ['option', 'interview']


admin.site.register(Choice, ChoiceAdmin)
