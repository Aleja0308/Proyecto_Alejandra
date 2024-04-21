from django import forms
from .models import Basica
from .models import Medica
from .models import Documento
from .models import Genero
from .models import Sangre
from .models import Hijos
from .models import Estado
from .models import Ocupacion


#Se define el formulario para Documento:
class DocumentoForm(forms.ModelForm):
  class Meta:
    model = Documento
    fields = ['documento']
    widgets = {'documento': forms.Select(attrs={'class':'form__control'})}


#Se define el formulario para Genero:
class GeneroForm(forms.ModelForm):
  class Meta:
    model = Genero
    fields = ['genero']
    widgets = {'genero': forms.Select(attrs={'class':'form__control'})}


#Se define el formulario para Sangre:
class SangreForm(forms.ModelForm):
  class Meta:
    model = Sangre
    fields = ['sangre']
    widgets = {'sangre': forms.Select(attrs={'class':'form__control'})}


#Se define el formulario para Hijos:
class HijosForm(forms.ModelForm):
  class Meta:
    model = Hijos
    fields = ['hijos']
    widgets = {'hijos': forms.Select(attrs={'class':'form__control'})}


#Se define el formulario para Estado:
class EstadoForm(forms.ModelForm):
  class Meta:
    model = Estado
    fields = ['estado']
    widgets = {'estado': forms.Select(attrs={'class':'form__control'})}


#Se define el formulario para Ocupacion:
class OcupacionForm(forms.ModelForm):
  class Meta:
    model = Ocupacion
    fields = ['ocupacion']
    widgets = {'ocupacion': forms.Select(attrs={'class':'form__control'})}


#Se define el formulario para Basica:
class BasicaForm(forms.ModelForm): 
  class Meta:
    model = Basica
    fields = ['documento','num_documento','nombres','apellidos','fecha_nacimiento','lugar_nacimiento','telefono','correo_electronico','direccion_residencia','edad','genero','estatura','peso','sangre','hijos','estado','ocupacion']
    widgets = {
      'documento': forms.Select(attrs={'class':'form__control'}),
      'num_documento': forms.NumberInput(attrs={'type':'number','class':'form__control'}),
      'nombres': forms.TextInput(attrs={'type':'text','class':'form__control'}),
      'apellidos': forms.TextInput(attrs={'type':'text','class':'form__control'}),
      'fecha_nacimiento': forms.DateInput(attrs={'type':'date','class':'form__control'}),
      'lugar_nacimiento': forms.TextInput(attrs={'type':'text','class':'form__control'}),
      'telefono': forms.NumberInput(attrs={'type':'tel','class':'form__control'}),
      'correo_electronico': forms.EmailInput(attrs={'type':'email','class':'form__control'}),
      'direccion_residencia': forms.TextInput(attrs={'type':'text','class':'form__control'}),
      'edad': forms.NumberInput(attrs={'type':'number','class':'form__control'}),
      'genero': forms.Select(attrs={'class':'form__control'}),
      'estatura': forms.NumberInput(attrs={'type':'number','class':'form__control'}),
      'peso': forms.NumberInput(attrs={'type':'number','class':'form__control'}),
      'sangre': forms.Select(attrs={'class':'form__control'}),
      'hijos': forms.Select(attrs={'class':'form__control'}),
      'estado': forms.Select(attrs={'class':'form__control'}),
      'ocupacion': forms.Select(attrs={'class':'form__control'}),
    }


#Se define el formulario para Medica.
class MedicaForm(forms.ModelForm):
  class Meta:
    model = Medica
    fields = ['historial_medico','sistematologia_actual','medicamentos_actuales','examenes_laboratorio','examenes_imagenologia','antecedentes_familiares','antecedentes_personales','tension_arterial','glucemia','sat_O2']
    widgets = {
    'historial_medico': forms.Textarea(attrs={'type':'text','class':'form__control'}),
    'sistematologia_actual': forms.Textarea(attrs={'type':'text','class':'form__control'}),
    'medicamentos_actuales': forms.Textarea(attrs={'type':'text','class':'form__control'}),
    'examenes_laboratorio': forms.Textarea(attrs={'type':'text','class':'form__control'}),
    'examenes_imagenologia': forms.Textarea(attrs={'type':'text','class':'form__control'}),
    'antecedentes_familiares': forms.Textarea(attrs={'type':'text','class':'form__control'}),
    'antecedentes_personales': forms.Textarea(attrs={'type':'text','class':'form__control'}),
    'tension_arterial': forms.TextInput(attrs={'type':'text','class':'form__control'}),
    'glucemia': forms.TextInput(attrs={'type':'text','class':'form__control'}),
    'sat_O2': forms.TextInput(attrs={'type':'text','class':'form__control'}),
    }