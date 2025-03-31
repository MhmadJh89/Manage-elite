from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devices', views.devices, name='devices'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]