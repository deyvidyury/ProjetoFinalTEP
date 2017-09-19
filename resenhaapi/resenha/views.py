from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import *
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter

class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = "user-list"
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly, UsuarioOuSomenteLeitura,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = "user-detail"
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,UsuarioOuSomenteLeitura,)

class LivroList(generics.ListCreateAPIView):
  queryset = Livro.objects.all()
  serializer_class = LivroSerializer
  name = "livro-list"
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,UsuarioOuSomenteLeitura,)
  filter_fields = ('nome','autor','ano','editora',)
  search_fields = ('^nome',)
  ordering_fields = ('nome','autor','ano',)

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Livro.objects.all()
  serializer_class = LivroDetailSerializer
  name = "livro-detail"
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,UsuarioOuSomenteLeitura,)

class ResenhaList(generics.ListCreateAPIView):
  queryset = Resenha.objects.all()
  serializer_class = ResenhaSerializer
  name = "resenha-list"
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,DonoResenhaOuSomenteLeitura,)
  filter_fields = ('livro','dono','criado')
  search_fields = ('^livro',)
  ordering_fields = ('livro','dono','criado',)

  def perform_create(self, serializer):
    serializer.save(dono=self.request.user)  

class ResenhaDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Resenha.objects.all()
  serializer_class = ResenhaDetailSerializer
  name = "resenha-detail"
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,DonoResenhaOuSomenteLeitura,)

class ComentarioList(generics.ListCreateAPIView):
  queryset = Comentario.objects.all()
  serializer_class = ComentarioSerializer
  name = "comentario-list"
  permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comentario.objects.all()
  serializer_class = ComentarioSerializer
  name = "comentario-detail"
  permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class AvaliacaoList(generics.ListCreateAPIView):
  queryset = Avaliacao.objects.all()
  serializer_class = AvaliacaoSerializer
  name = 'avaliacao-list'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly)

  def perform_create(self, serializer):
    serializer.save(usuario=self.request.user) 

class AvaliacaoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Avaliacao.objects.all()
  serializer_class = AvaliacaoSerializer
  name = 'avaliacao-detail'
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,DonoResenhaOuSomenteLeitura)

class ApiRoot(generics.GenericAPIView):
  name = 'api-root'
  def get(self, request, *args, **kwargs):
    return Response({
      'users': reverse(UserList.name, request=request),
      'livros': reverse(LivroList.name, request=request),
      'resenhas': reverse(ResenhaList.name, request=request),
      'comentarios': reverse(ComentarioList.name, request=request),
      'avaliacoes': reverse(AvaliacaoList.name, request=request)
    })