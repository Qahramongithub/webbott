from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.forms import TimeInput

from apps.models import  Meeting

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("fullname", "phone_number", "formatted_date", "formatted_time", "status", "operator", "description")
    list_editable = ("status",)
    search_fields = ("fullname", "phone_number", "description",)
    list_filter = ("date", "status",)
    ordering = ("date",)

    def formatted_date(self, obj):
        return obj.date.strftime('%Y-%m-%d')
    formatted_date.short_description = "Sana"

    def formatted_time(self, obj):
        return obj.time.strftime('%H:%M:%S')

    formatted_time.short_description = "Vaqt"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['time'].widget = TimeInput(attrs={'type': 'time'})  # HTML5 time picker
        return form

admin.site.unregister(User)
admin.site.unregister(Group)
