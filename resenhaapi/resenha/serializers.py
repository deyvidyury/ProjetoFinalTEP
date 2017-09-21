from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserResenhaSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Resenha
    fields = ('url','id','dono')

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
    write_only_fields = ('password',)
    read_only_fields = ('id',)

  def create(self, validated_data):
    user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name']
    )

    user.set_password(validated_data['password'])
    user.save()

    return user

class UserSerializer(serializers.HyperlinkedModelSerializer):
  resenhas = UserResenhaSerializer(read_only=True, many=True, required=False)

  class Meta:
    model = User
    fields = ('url',
              'id',
              'username',
              'email',
              'password',
              'resenhas')

    write_only_fields = ('password',)

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email']
    )

    user.set_password(validated_data['password'])
    user.save()

    return user

class LivroResenhasSerializer(serializers.HyperlinkedModelSerializer):
  dono = serializers.ReadOnlyField(source='dono.username')

  class Meta:
    model = Resenha
    fields = ('url',
              'id',
              'dono',
              'criado',
              'nota',
              'texto')

class LivroSerializer(serializers.HyperlinkedModelSerializer):
  resenhas = LivroResenhasSerializer(read_only=True, many=True, required=False)

  class Meta:
    model = Livro
    fields = ('url',
              'id',
              'nome',
              'autor',
              'ano',
              'editora',
              'criado',
              'atualizado',
              'isbn',
              'resenhas')

class LivroDetailSerializer(serializers.HyperlinkedModelSerializer):
  resenhas = LivroResenhasSerializer(read_only=True, many=True, required=False)

  class Meta:
    model = Livro
    fields = ('url',
              'id',
             'nome',
             'autor',
             'ano',
             'editora',
             'criado',
             'atualizado',
             'isbn',
             'resenhas')

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Comentario
    fields = ('url',
              'id',
              'nome',
              'email',
              'comentario',
              'resenha',
              'criado')

class ResenhaSerializer(serializers.HyperlinkedModelSerializer):
  dono = serializers.ReadOnlyField(source='dono.username')
  # livro = serializers.SlugRelatedField(queryset=Livro.objects.all(),slug_field='nome')
  livro = LivroSerializer(read_only=True)
  comentarios = ComentarioSerializer(many=True,read_only=True)

  class Meta:
    model = Resenha
    fields = ('url',
              'id',
              'livro',
              'texto',
              'dono',
              'criado',
              'atualizado',
              'nota',
              'comentarios')

class ResenhaDetailSerializer(serializers.HyperlinkedModelSerializer):
  dono = serializers.ReadOnlyField(source='dono.username')
  livro = serializers.SlugRelatedField(queryset=Livro.objects.all(),slug_field='nome')
  comentarios = ComentarioSerializer(many=True,read_only=True)

  class Meta:
    model = Resenha
    fields = ('url',
              'id',
              'livro',
              'texto',
              'dono',
              'criado',
              'nota',
              'atualizado',
              'comentarios')

class AvaliacaoSerializer(serializers.HyperlinkedModelSerializer):
  resenha = serializers.SlugRelatedField(queryset=Resenha.objects.all(),slug_field='id')
  estrelas = serializers.ChoiceField(choices = Avaliacao.STARS)
  # usuario = serializers.ReadOnlyField(source='usuario.username')

  class Meta:
    model = Avaliacao
    fields = ('url',
              'id',
              'resenha',
              'estrelas')