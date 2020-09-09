from django import forms
import reservas_web.settings

from .models import Reserva,Local,Horario,Visita,Persona


class ReservaForm(forms.ModelForm):
    fecha_reserva = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y',attrs={'class':'form-control datetime-input'}), input_formats=reservas_web.settings.DATE_INPUT_FORMATS)

    lugar_reserva = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),
                                           queryset=Local.objects.all(), initial=0)

    hora_reserva = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                           queryset=Horario.objects.all(), initial=0)

    cant_personas_reserva = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                               label='Cantidad de Personas')

    titular_nombre_reserva = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombre del Titular')

    titular_apellido_reserva = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Apellido del Titular')

    titular_nro_telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Telefono del Titular')

    titular_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email del Titular')

    titular_comentarios = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',"rows":5, "cols":20,
                                                                       'placeholder': 'Ubicacion en el Local, '
                                                                                      'Es un cumpleaños?'}),
                                          label='Comentarios para la Reserva',required=False)

    class Meta:
        model = Reserva
        fields = ('fecha_reserva','lugar_reserva',
                  'hora_reserva',
                  'cant_personas_reserva',
                  'titular_nombre_reserva',
                  'titular_apellido_reserva',
                  'titular_nro_telefono',
                  'titular_email',
                  'titular_comentarios')


class VisitaForm(forms.ModelForm):
    cumpleanos_persona = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control datetime-input'}),
        input_formats=reservas_web.settings.DATE_INPUT_FORMATS,
        label='Fecha de Nacimiento')

    cedula_persona = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                               label='Numero de Cedula')
    nombre_persona = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombre')
    apellido_persona = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellido')
    direccion_persona = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Direccion particular')
    ciudad_persona = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Ciudad')
    barrio_persona = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Barrio')
    nro_telefono_persona = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nro de Telefono')
    email_persona = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Correo Electronico')



    class Meta:
        model = Persona
        fields = (
                  'cedula_persona',
                  'nombre_persona',
                  'apellido_persona',
                  'direccion_persona',
                  'ciudad_persona',
                  'barrio_persona',
                  'nro_telefono_persona',
                  'email_persona',
                  'cumpleanos_persona',)


class VisitaRealForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'

