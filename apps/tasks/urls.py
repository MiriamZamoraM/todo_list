from django.urls import path
from .views import TaskReg, Retrieve, Update, Delete

urlpatterns = [
    path('reg/', TaskReg.as_view(), name='Registro de tareas'),
    path('view/', Retrieve.as_view(), name='Vista de tareas'),
    path('update/<int:id>/', Update.as_view(), name='Actualizar tarea'),
    path('delete/<int:id>/', Delete.as_view(), name='Eliminar tarea'),
]