from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


    def alternar_activo(self, commit=True):
        self.activo = not self.activo
        
        if commit:
            self.save(update_fields=['activo', 'last_update'])
        
        return self.activo


    def __str__(self):
        return f'{self.nombre} {self.apellido}'
