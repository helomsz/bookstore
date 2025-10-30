from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('Autores', AutoresView.as_view()),
    path('Autores', visualizacao_autor),
    path('Editoras', EditoraView.as_view()),
    path('Livros', LivroView.as_view()),
    path('Buscar/', AutoresView.as_view()),

    #UPTADE / DELETE
    path('autor/<int:pk>', AutoresDetailView.as_view()),
    path('editora/<int:pk>', EditoraDetailView.as_view()),
    path('livro/<int:pk>', LivroDetailView.as_view()),

    #TOKEN
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

