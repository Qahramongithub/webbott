from django.db import models
from django.db.models import Model, SET_NULL


class Operator(Model):
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.fullname


class Meeting(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = 'new', "Yangi"
        SOLD_OUT = 'sold_out', 'Sotildi'
        SOLD_NOT = 'sold_not', 'Sotilmadi'
        ARCHIVED = 'archived', 'Archived'
        MEETING = 'uchrashuv_belgilandi', 'Uchrashuv belgilandi'

    status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.NEW)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=50)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    operator = models.ForeignKey('apps.Operator', on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Meeting: {self.fullname}"
