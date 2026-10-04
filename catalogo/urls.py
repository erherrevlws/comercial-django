from django.urls import path
from .views.categoria import lista_categorias

urlpatterns = [
    path('categorias/', lista_categorias, name='lista_categorias'),
]