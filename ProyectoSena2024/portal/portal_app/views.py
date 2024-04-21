from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Basica
from .models import Medica
from .forms import BasicaForm
from .forms import MedicaForm
from .forms import DocumentoForm
from .forms import GeneroForm
from .forms import SangreForm
from .forms import HijosForm
from .forms import EstadoForm
from .forms import OcupacionForm

# Create your views here.
  
def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    #Autenticar al usuario utilizando el nombre del usuario y el documento de identidad:
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('read_inicio')
    else:
      return redirect('login')
  else:
    return render(request, 'layouts/login.html', {})

@login_required
def index(request):
  return render(request, 'layouts/index.html', {})

#Se define la vista de Documento:
#CREATE:
@login_required
def add_documento(request):
  if request.method == 'POST':
    form = DocumentoForm(request.POST)
    if form.is_valid():
      documento = form.save()
      return render(request, 'options/documento.html', {'documento': documento})
  else:
    form = DocumentoForm()
    return render(request, 'options/documento.html', {'form': form})


#Se define la vista de Genero:
#CREATE:
@login_required
def add_genero(request):
  if request.method == 'POST':
    form = GeneroForm(request.POST)
    if form.is_valid():
      genero = form.save()
      return render(request, 'options/genero.html', {'genero': genero})
  else:
    form = GeneroForm()
    return render(request, 'options/genero.html', {'form': form})


#Se define la vista de Sangre:
#CREATE:
@login_required
def add_sangre(request):
  if request.method == 'POST':
    form = SangreForm(request.POST)
    if form.is_valid():
      sangre = form.save()
      return render(request, 'options/sangre.html', {'sangre': sangre})
  else:
    form = SangreForm()
    return render(request, 'options/sangre.html', {'form': form})


#Se define la vista de Hijos:
#CREATE:
@login_required
def add_hijos(request):
  if request.method == 'POST':
    form = HijosForm(request.POST)
    if form.is_valid():
      hijos = form.save()
      return render(request, 'options/hijos.html', {'hijos': hijos})
  else:
    form = HijosForm()
    return render(request, 'options/hijos.html', {'form': form})


#Se define la vista de Estado:
#CREATE:
@login_required
def add_estado(request):
  if request.method == 'POST':
    form = EstadoForm(request.POST)
    if form.is_valid():
      estado = form.save()
      return render(request, 'options/estado.html', {'estado': estado})
  else:
    form = EstadoForm()
    return render(request, 'options/estado.html', {'form': form})


#Se define la vista de Ocupacion:
#CREATE:
@login_required
def add_ocupacion(request):
  if request.method == 'POST':
    form = OcupacionForm(request.POST)
    if form.is_valid():
      ocupacion = form.save()
      return render(request, 'options/ocupacion.html', {'ocupacion': ocupacion})
  else:
    form = OcupacionForm()
    return render(request, 'options/ocupacion.html', {'form': form})


#Se define la vista de Basica:
#CREATE:
@login_required
def add_basica(request):
    if request.method == 'POST':
        form = BasicaForm(request.POST)
        if form.is_valid():
          basica_instance = form.save(commit=False)
          basica_instance.save()
          return redirect('add_medica', basica_id=basica_instance.id)
    else:
        form = BasicaForm()  #Se crea un formulario vacío para solicitudes GET
    return render(request, 'forms/basica.html', {'form': form})

#READ read_inicio:
@login_required
def read_inicio(request):
    basicas = Basica.objects.all()
    return render(request, 'read_inicio.html', {'basicas': basicas})

#READ read_basica:
@login_required
def read_basica(request):
    basicas = Basica.objects.all()
    return render(request, 'read_basica.html', {'basicas': basicas})

#UPDATE:
@login_required
def update_basica(request, pk):
    basica = get_object_or_404(Basica, pk=pk)
    if request.method == 'POST':
        form = BasicaForm(request.POST, instance=basica)
        if form.is_valid():
            form.save()
            return redirect('update_medica')
    else:
        form = BasicaForm(instance=basica)
    return render(request, 'forms/update_basica.html', {'form': form, 'basica': basica})

#DELETE:
@login_required
def delete_basica(request, pk):
    basica = get_object_or_404(Basica, pk=pk)
    if request.method == 'POST':
        basica.delete()
        return redirect('read_basica')
    return render(request, 'forms/delete_basica.html', {'basica': basica})


#Se define la vista de Medica:
#CREATE:
@login_required
def add_medica(request, basica_id=None):
    basica_instance = Basica.objects.get(pk=basica_id)
    if request.method == 'POST':
        form = MedicaForm(request.POST)
        if form.is_valid():
          medica_instance = form.save(commit=False)
          medica_instance.basica = basica_instance
          medica_instance.save()
        return redirect('read_inicio')
    else:
        form = MedicaForm()  #Se crea un formulario vacío para solicitudes GET
    return render(request, 'forms/medica.html', {'form': form, 'basica_id': basica_id})


#READ:
@login_required
def read_medica(request):
    medicas = Medica.objects.all()
    return render(request, 'read_medica.html', {'medicas': medicas})


#UPDATE:
@login_required
def update_medica(request, pk):
    medica = get_object_or_404(Medica, pk=pk)
    if request.method == 'POST':
        form = MedicaForm(request.POST, instance=medica)
        if form.is_valid():
            form.save()
            return redirect('read_inicio')
    else:
        form = MedicaForm(instance=medica)
    return render(request, 'forms/update_medica.html', {'form': form, 'medica': medica})

#DELETE:
@login_required
def delete_medica(request, pk):
    medica = get_object_or_404(Medica, pk=pk)
    if request.method == 'POST':
        medica.delete()
        return redirect('read_medica')
    return render(request, 'forms/delete_medica.html', {'medica': medica})
  
#LOGOUT:

def logout_session(request):
  logout(request)
  return redirect('login')