from django.contrib import admin
from .models import Local,Horario,Reserva,Persona,Visita
from django.contrib.admin import DateFieldListFilter

from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


# Register your models here.


admin.site.register(Local)
admin.site.register(Horario)
admin.site.register(Persona)



class ReservaAdmin(admin.ModelAdmin):
    list_display = (('lugar_reserva'), ('fecha_reserva'), ('hora_reserva'), ('cant_personas_reserva'),
                    ('titular_nombre_reserva'),
                    ('titular_apellido_reserva'), ('titular_nro_telefono'),('titular_comentarios'),('utilizado'),('activo'),)
    search_fields = (('fecha_reserva'), ('hora_reserva__hora_posibles'), ('cant_personas_reserva'),
                     ('titular_nombre_reserva'), ('titular_apellido_reserva'),('titular_nro_telefono'),('titular_comentarios'),)

    list_filter = (
        ('fecha_reserva', DateRangeFilter),
        ('utilizado'),
        ('activo'),
    )

admin.site.register(Reserva,ReservaAdmin)


class VisitaAdmin(admin.ModelAdmin):
    list_display = (('fechahora_visita','persona','mesa_asignada','activo'))

    list_filter = (
        ('fechahora_visita', DateRangeFilter),
        ('activo'),
        ('mesa_asignada'),

    )

admin.site.register(Visita,VisitaAdmin)