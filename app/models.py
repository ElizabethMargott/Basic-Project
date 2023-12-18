from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    img = models.ImageField(upload_to='proyectos/')

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
