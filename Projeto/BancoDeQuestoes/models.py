from django.db import models

class Disciplina(models.Model):
  nome = models.CharField(max_length=200)

  def __str__(self):
    return self.nome

class Serie(models.Model):
  nome = models.CharField(max_length=200)

  def __str__(self):
    return self.nome

class Alternativa(models.Model):
  ALTERNATIVAS_CHOICES = (
    (C, 'Correta'),
    (E, 'Errada')
  )
  texto = models.TextField()
  valor = models.CharField(max_length=2, choices=ALTERNATIVAS_CHOICES, default=C)
  questao = models.ForeignKey(Questao, related_name='alternativas', on_delete=models.CharField)

  def __str__(self):
    return self.texto

class Questao(models.Model):
  OBJECTIVA = 'O'
  SUBJECTIVA = 'S'
  
  TIPO_CHOICES = (
    (OBJECTIVA,'Objetiva'),
    (SUBJETIVA,'Subjetiva'),
  )

  enunciado = models.TextField()
  imagem = models.CharField(max_length=300)
  disciplina = models.ForeignKey(Disciplina, related_name='questoes_disciplina',models.SET_NULL,blank=True,null=True)
  serie = models.ForeignKey(Serie, related_name="questoes_serie",models.SET_NULL,blank=True,null=True)
  atividade = models.ForeignKey(Atividade, related_name='questoes', models.SET_NULL,blank=True,null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  tipo = models.CharField(
    max_length=2,
    choices=TIPO_CHOICES,
    default=OBJETIVA,
  )
  owner = models.ForeignKey('auth.User',related_name='questoes',models.SET_NULL,blank=True,null=True)

  def __str__(self):
    return self.enunciado

class Atividade(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  disciplina = models.ForeignKey(Disciplina, related_name='atividades_disciplina',models.SET_NULL,blank=True,null=True)
  serie = models.ForeignKey(Serie, related_name="atividades_serie",models.SET_NULL,blank=True,null=True)
  owner = models.ForeignKey('auth.User',related_name='atividades',models.SET_NULL,blank=True,null=True)

  class Meta:
    ordering = ('-created_at',)