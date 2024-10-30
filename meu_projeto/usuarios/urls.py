from django.urls import path
from .views import registrar_usuario, sucesso

urlpatterns = [
    path('registrar/', registrar_usuario, name='registrar_usuario'),  # URL para registrar usuário
    path('sucesso/', sucesso, name='sucesso'),  # URL para a página de sucesso
]
