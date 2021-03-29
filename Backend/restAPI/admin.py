from django.contrib import admin
from .models import Human

class HumanAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', )

admin.site.register(Human, HumanAdmin)

