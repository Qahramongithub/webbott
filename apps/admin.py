import telebot
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.forms import TimeInput

from apps.models import Meeting

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("fullname", "phone_number", "formatted_date", "formatted_time", "status", "operator", "description")
    list_editable = ("status",)
    search_fields = ("fullname", "phone_number", "description", 'operator__fullname',)
    list_filter = ("date", "status", 'operator__fullname')
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

    def save_model(self, request, obj, form, change,):
        bot = telebot.TeleBot("7725923661:AAEwEvqw7V6icuD2t9f7jTiK_LfdD-AaMV8")
        fullname = obj.fullname
        phone_number = obj.phone_number
        date = obj.date
        time = obj.time
        status = obj.get_status_display()
        description = obj.description
        operator = obj.operator

        text = (
            f"👤 FSHI: {fullname}\n"
            f"📞 Telefon: {phone_number}\n"
            f"📅 Sana: {date}\n"
            f"🕔 Vaqt: {time}\n"
            f"📊 Holat: {status}\n"
            f"📁 Izoh: {description}\n"
            f"🤵‍♂️ Operator: {operator}\n"
        )

        try:
            bot.send_message(chat_id=-1002271581092, text=text)
        except Exception as e:
            pass

        return super().save_model(request, obj, form, change)

admin.site.unregister(User)
admin.site.unregister(Group)
