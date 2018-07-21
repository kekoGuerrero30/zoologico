from django.db import models

class Visitantes(models.Model):
	Nombre=models.CharField(max_length=60, help_text='Nombre')
	Apellido=models.CharField(max_length=60, help_text='Apellido')

	def __str__(self):
		return self.Nombre

class Vacunas(models.Model):
	Tipo_de_vacuna=models.CharField(max_length=50, help_text='Nombre de la vacuna')
	Fecha_de_vencimiento=models.DateField(help_text='Fecha de vencimiento de la vacuna')

	def __str__(self):
		return self.Tipo_de_vacuna

class Animales(models.Model):
	Tipo_de_animal=models.CharField(max_length=50, help_text='Tipo de animal')
	Edad=models.CharField(max_length=3, help_text='Edad del animal')
	Vacunas=models.ForeignKey(Vacunas, on_delete=models.CASCADE)

	def __str__(self):
		return self.Tipo_de_animal

class Empleados(models.Model):
	Nombre_del_empleado=models.CharField(max_length=60, help_text='Nombre del empleado')
	Cargo=models.CharField(max_length=30, help_text='Cargo del empleado')

	def __str__(self):
		return self.Nombre_del_empleado

class Alimentacion(models.Model):
	Tipo_de_alimento=models.CharField(max_length=100, help_text='Tipo de alimento')
	Precio=models.CharField(max_length=120, help_text='Precio del alimento')
	Cantidad=models.CharField(max_length=120, help_text='Cantidad de alimento')

	def __str__(self):
		return self.Tipo_de_alimento

class Historial_de_Vacunas(models.Model):
	Nombre_de_la_vacuna=models.CharField(max_length=100, help_text='Nombre de la vacuna')
	Cantidad=models.CharField(max_length=120, help_text='Cantidad del producto')
	Fecha_de_aplicacion=models.DateField(help_text='Fecha de aplicacion de la vacuna')
	Dosis=models.CharField(max_length=50, help_text='Dosis de la vacuna')
	Animal=models.ForeignKey(Animales, on_delete=models.CASCADE)

	def __str__(self):
		return self.Nombre_de_la_vacuna