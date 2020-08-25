from django.db import models

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

    class Meta:
        verbose_name= 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return self.titular_apellido_reserva + ', ' + self.titular_nombre_reserva + ' '+str(self.fecha_reserva)

