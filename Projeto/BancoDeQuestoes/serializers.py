from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class DisciplinaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Disciplina
    fields = ('url','nome')

class SerieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Serie
    fields = ('url','nome')

class AlternativaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Alternativa
    fields = ('url','text','valor')

class QuestaoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Questao
    fields = ('url','enunciado','imagem','disciplina','serie','created_at')
