from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('busca/', views.busca, name='busca'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
]