from django.contrib import admin
from .models import CognitiveModel


class CognitiveAdmin(admin.ModelAdmin):
    list_display = ('text',)


# Register your models here.

admin.site.register(CognitiveModel, CognitiveAdmin)
