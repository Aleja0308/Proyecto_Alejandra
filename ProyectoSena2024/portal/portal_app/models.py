from django.db import models

# Create your models here.

#Se define modelos Documento:
class Documento(models.Model):
  ROLES_CHOICES = (
    ('CC','CC'),
    ('TI','TI'),
    ('RC','RC'),
    ('CE','CE'),
    ('PEP','PEP'),
    ('DNI','DNI'),
    ('SCR','SCR'),
    ('PA','PA'),
  )
  documento = models.CharField(max_length=20, choices=ROLES_CHOICES)
  def __str__(self):
    return self.documento

#Se define modelos Genero:
class Genero(models.Model):
  ROLES_CHOICES = (
    ('Femenino','Femenino'),
    ('Masculino','Masculino'),
    ('Intersexual','Intersexual'),
    ('Otro','Otro'),
  )
  genero = models.CharField(max_length=20, choices=ROLES_CHOICES)
  def __str__(self):
    return self.genero


#Se define modelos Sangre:
class Sangre(models.Model):
  ROLES_CHOICES = (
    ('O+','O+'),
    ('O-','O-'),
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
  )
  sangre = models.CharField(max_length=20, choices=ROLES_CHOICES)
  def __str__(self):
    return self.sangre


#Se define modelos Hijos:
class Hijos(models.Model):
  ROLES_CHOICES = (
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5 o más','5 o más'),
  )
  hijos = models.CharField(max_length=20, choices=ROLES_CHOICES)
  def __str__(self):
    return self.hijos


#Se define modelos Estado:
class Estado(models.Model):
  ROLES_CHOICES = (
    ('Soltero(a)','Soltero(a)'),
    ('Unión libre','Unión libre'),
    ('Casado(a)','Casado(a)'),
    ('Divorciado(a)','Divorciado(a)'),
    ('Viudo(a)','Viudo(a)'),
  )
  estado = models.CharField(max_length=20, choices=ROLES_CHOICES)
  def __str__(self):
    return self.estado


#Se define modelos Ocupacion:
class Ocupacion(models.Model):
  ROLES_CHOICES = (
    ('Desempleado(a)','Desempleado(a)'),
    ('Empleado(a)','Empleado(a)'),
    ('Independiente','Independiente'),
  )
  ocupacion = models.CharField(max_length=20, choices=ROLES_CHOICES)
  def __str__(self):
    return self.ocupacion


#Se define modelos Basica:
class Basica (models.Model):
  documento = models.ForeignKey(Documento, on_delete = models.CASCADE, null=True)
  num_documento = models.IntegerField(null=True)
  nombres = models.CharField(max_length=50)
  apellidos = models.CharField(max_length=50)
  fecha_nacimiento = models.DateField()
  lugar_nacimiento = models.CharField(max_length=50)
  telefono = models.IntegerField()
  correo_electronico = models.EmailField()
  direccion_residencia = models.CharField(max_length=100)
  edad = models.IntegerField()
  genero = models.ForeignKey(Genero, on_delete = models.PROTECT, null= True)
  estatura = models.FloatField()
  peso = models.FloatField()
  sangre = models.ForeignKey(Sangre, on_delete = models.PROTECT, null= True)
  hijos = models.ForeignKey(Hijos, on_delete = models.PROTECT, null= True)  
  estado = models.ForeignKey(Estado, on_delete = models.PROTECT, null= True)
  ocupacion = models.ForeignKey(Ocupacion, on_delete = models.PROTECT, null= True)


#Se define modelos Medica:
class Medica (models.Model):
  basica = models.OneToOneField(Basica, on_delete = models.CASCADE, null=True)
  historial_medico = models.TextField(max_length=250)
  sistematologia_actual = models.TextField(max_length=250)
  medicamentos_actuales = models.TextField(max_length=250)
  examenes_laboratorio = models.TextField(max_length=250)
  examenes_imagenologia = models.TextField(max_length=250)
  antecedentes_familiares = models.TextField(max_length=250)
  antecedentes_personales = models.TextField(max_length=250)
  tension_arterial = models.FloatField()
  glucemia = models.FloatField()
  sat_O2 = models.IntegerField()