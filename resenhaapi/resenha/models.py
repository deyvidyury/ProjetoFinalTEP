from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

class Livro(models.Model):
  nome = models.CharField(max_length=200)
  autor = models.CharField(max_length=200)
  ano = models.IntegerField(blank=True,null=True)
  editora = models.CharField(max_length=200,blank=True,null=True)
  criado = models.DateTimeField(auto_now_add=True)
  atualizado = models.DateTimeField(null=True)
  isbn = models.CharField(max_length=100,blank=True, null=True, default='')

  @property
  def resenhas(self):
    return Resenha.objects.filter(livro = self.id)

class Resenha(models.Model):
  dono = models.ForeignKey(User, related_name='resenhas', on_delete=models.CASCADE)
  livro = models.ForeignKey(Livro, related_name="livro")
  texto = models.TextField()
  criado = models.DateTimeField(auto_now_add=True)
  atualizado = models.DateTimeField(null=True)

  @property
  def nota(self):
    return Avaliacao.objects.filter(resenha = self.id).aggregate(Avg('estrelas'))

  class Meta:
    ordering = ('criado',)

  def __str__(self):
    return self.livro.nome

class Comentario(models.Model):
  nome = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  comentario = models.TextField()
  resenha = models.ForeignKey(Resenha, related_name="comentarios", on_delete=models.CASCADE)
  criado = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return "Comentario de %s: \"%s\"" % self.nome, self.comentario

class Avaliacao(models.Model):
  STARS = (
    (1, 'Um'),
    (2, 'Duas'),
    (3, 'Tres'),
    (4, 'Quatro'),
    (5, 'Cinco')
  )
  estrelas = models.CharField(max_length=2,choices=STARS)
  resenha = models.ForeignKey(Resenha)
  # usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  # usuario = models.ForeignKey('auth.User')

