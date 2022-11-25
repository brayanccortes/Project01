from django.contrib import admin

from .models import Persona

# Register your models here.

class AdminPersona(admin.ModelAdmin):
    list_display = ["id","nombres","apellidos","correo"]
    list_filter = ["nombres","apellidos","correo"]
    list_editable = ["nombres", "apellidos", "correo"]
    search_fields = ["correo"]
    class Meta:
        models = Persona

admin.site.register(Persona, AdminPersona)