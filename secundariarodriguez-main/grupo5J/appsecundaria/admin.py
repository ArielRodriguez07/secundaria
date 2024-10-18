from django.contrib import admin
from .models import AlumnoT,Frase
# Register your models here.

class 

admin.site.register(AlumnoT,AlumnoAdmin)

class comentarioIntLine (admin.TabularInline):
    model = Frase
    extra=1

class AlumnoAdmin(admin.ModelAdmin):
    fields=["apaterno","amaterno","fecha_nacimiento","fecha_ingreso"]
    list_display=["apaterno","amaterno","nombre"]
    inlines=[comentarioIntLine]