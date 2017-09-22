from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

from .views import *

urlpatterns = [
  url(r'^docs/', include_docs_urls(title='My API title')),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'^api-token/', views.obtain_auth_token, name='api-token'),
  # url(r'^api-token/', SFObtainAuthToken.as_view()),
  url(r'^$', ApiRoot.as_view(), name='root'),
  url(r'^users/$',
      UserList.as_view(),
      name=UserList.name),
  url(r'^users/(?P<pk>[0-9]+)/$',
      UserDetail.as_view(),
      name=UserDetail.name),
  url(r'^livros/$',
      LivroList.as_view(),
      name=LivroList.name),
  url(r'^livros/(?P<pk>[0-9]+)/$',
      LivroDetail.as_view(),
      name=LivroDetail.name),
  url(r'^resenhas/$',
      ResenhaList.as_view(),
      name=ResenhaList.name),
  url(r'^resenhas/(?P<pk>[0-9]+)/$',
      ResenhaDetail.as_view(),
      name=ResenhaDetail.name),
  url(r'^comentarios/$',
      ComentarioList.as_view(),
      name=ComentarioList.name),
  url(r'^comentarios/(?P<pk>[0-9]+)/$',
      ComentarioDetail.as_view(),
      name=ComentarioDetail.name),
  url(r'^avaliacoes/$',
      AvaliacaoList.as_view(),
      name=AvaliacaoList.name),
  url(r'^avaliacoes/(?P<pk>[0-9]+)/$',
      AvaliacaoDetail.as_view(),
      name=AvaliacaoDetail.name),
]