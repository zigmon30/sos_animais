from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Animal(models.Model):
    cidade = models.CharField(max_length=100)
    descricao = models.TextField()
    telefone = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_final = models.DateTimeField(null=True, blank=True)
    data_inicial = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='animal')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'animal_para_adocao'
