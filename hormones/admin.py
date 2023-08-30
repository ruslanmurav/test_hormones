from django.contrib import admin
from hormones.models import Hormone, Record, RecordValue


@admin.register(Hormone)
class HormoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass


@admin.register(RecordValue)
class RecordValueAdmin(admin.ModelAdmin):
    pass




