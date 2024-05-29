from django.db import models
from users.models import User

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nombre de la tarea")
    st_op = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('finalizado', 'Finalizado'),
    ]
    status = models.CharField(choices=st_op, max_length=150, verbose_name="Estado de la tarea")
    created = models.DateTimeField(auto_now_add=True)
    limit = models.DateField(verbose_name="Fecha límite")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    status_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "tasks"
        verbose_name = "Tareas"