from django.contrib import admin
from voice.models import voice_qamodel
class QAModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in voice_qamodel._meta.local_fields]

admin.site.register(voice_qamodel, QAModelAdmin)