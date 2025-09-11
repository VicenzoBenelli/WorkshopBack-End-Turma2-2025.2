from django.db import models

# Create your models here.

from django.db import models

class Address(models.Model):
    cep = models.CharField(max_length=9, unique=True)  
    street = models.CharField(max_length=150, blank=True)
    neighborhood = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return f"{self.cep} - {self.street}, {self.neighborhood}, {self.city}/{self.state}"
