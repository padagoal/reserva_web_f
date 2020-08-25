from django.contrib import admin
from .models import Local,Horario,Reserva
# Register your models here.


admin.site.register(Local)
admin.site.register(Horario)


class ReservaAdmin(admin.ModelAdmin):
    list_display = (('lugar_reserva'), ('fecha_reserva'), ('hora_reserva'), ('cant_personas_reserva'),
                    ('titular_nombre_reserva'),
                    ('titular_apellido_reserva'), ('titular_nro_telefono'),('titular_comentarios'),)
    search_fields = (('fecha_reserva'), ('hora_reserva__hora_posibles'), ('cant_personas_reserva'),
                     ('titular_nombre_reserva'), ('titular_apellido_reserva'),('titular_nro_telefono'),('titular_comentarios'),)

admin.site.register(Reserva,ReservaAdmin)