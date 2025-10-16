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

    
    def __str__(self):
        return self.nombre
