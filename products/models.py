from django.db import models
from django.core.validators import MinValueValidator


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    stock = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


    def alternar_activo(self, commit=True):
        self.activo = not self.activo
        
        if commit:
            self.save(update_fields=['activo', 'last_update'])
        
        return self.activo

    
    def __str__(self):
        return self.nombre
