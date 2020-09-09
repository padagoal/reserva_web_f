from django.db import models
from django.utils import timezone
# Create your models here.


class Local(models.Model):
    nombre = models.CharField(max_length=255,verbose_name='Nombre Local')

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    hora_posibles = models.TimeField(verbose_name='Hora')

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = (('hora_posibles'),)

    def __str__(self):
        return str(self.hora_posibles)


class Reserva(models.Model):
    lugar_reserva = models.ForeignKey(Local,verbose_name='Lugar de Reserva',on_delete=models.DO_NOTHING,null=True,
                                      blank=True)
    fecha_reserva = models.DateField(verbose_name='Fecha de Reserva',null=True,blank=True)
    hora_reserva = models.ForeignKey(Horario,verbose_name='Hora de Reserva',on_delete=models.DO_NOTHING,null=True,blank=True)
    cant_personas_reserva = models.IntegerField(default=1,verbose_name='Cantidad Personas',null=True,blank=True)
    titular_nombre_reserva = models.CharField(max_length=255,verbose_name='Nombre Titular',null=True,blank=True)
    titular_apellido_reserva = models.CharField(max_length=255, verbose_name='Apellido Titular',null=True,blank=True)
    titular_email = models.EmailField(verbose_name='Email del Titular',null=True,blank=True)
    titular_nro_telefono = models.CharField(max_length=255, verbose_name='Telefono Titular',null=True,blank=True)
    titular_comentarios = models.TextField(max_length=500,verbose_name='Comentarios',null=True,blank=True)

    utilizado = models.BooleanField(default=False,blank=True,verbose_name='Fue utilizado?')
    activo = models.BooleanField(default=True,blank=True)

    created_at = models.DateTimeField(verbose_name='Creado el',auto_now_add=True)

    class Meta:
        verbose_name= 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ('-fecha_reserva','activo')

    def __str__(self):
        return self.titular_apellido_reserva + ', ' + self.titular_nombre_reserva + ' '+str(self.fecha_reserva)


class Persona(models.Model):
    cedula_persona = models.IntegerField(verbose_name='Nro Cedula')
    nombre_persona = models.CharField(verbose_name='Nombre',max_length=255)
    apellido_persona = models.CharField(verbose_name='Apellido', max_length=255)
    direccion_persona = models.CharField(verbose_name='Direccion Particular',max_length=500)
    ciudad_persona = models.CharField(verbose_name='Ciudad',max_length=255)
    barrio_persona = models.CharField(verbose_name='Barrio',max_length=255)
    nro_telefono_persona = models.CharField(verbose_name='Nro de Telefono',max_length=255)
    email_persona = models.EmailField(verbose_name='Correo Electronico')
    cumpleanos_persona = models.DateField(verbose_name='Fecha de Nacimiento')

    created_at = models.DateTimeField(verbose_name='Creado el', auto_now_add=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return str(self.cedula_persona) + ' ' + self.apellido_persona + ', ' + self.nombre_persona


class Visita(models.Model):
    fechahora_visita = models.DateTimeField(verbose_name='Fecha / Hora de Visita',default=timezone.now)
    persona = models.ForeignKey(Persona,on_delete=models.DO_NOTHING,verbose_name='Persona')
    mesa_asignada = models.IntegerField(verbose_name='Mesa Asignada',null=True,blank=True)

    activo = models.BooleanField(verbose_name='Activo',default=True)

    created_at = models.DateTimeField(verbose_name='Creado el', auto_now_add=True)

    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        ordering = ('-fechahora_visita', 'activo')

    def __str__(self):
        return str(self.fechahora_visita) + ' ' + self.persona.apellido_persona + ', ' + self.persona.nombre_persona