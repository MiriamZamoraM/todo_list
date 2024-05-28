from django.urls import path
from .views import Registry, Login, View

urlpatterns = [
    path('view/', View.as_view(), name='view'),
    path('registry/', Registry.as_view(), name='registry'),
    path('login/', Login.as_view(), name='login'),
]