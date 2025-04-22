from django.urls import include, path
from . import views

urlpatterns = [
    path('cadastrar', views.cadastrar, name="cadastrar"),
    path('excluir/<int:id>', views.exluir, name="exluir")
]