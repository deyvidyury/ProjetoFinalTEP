from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserResenhaSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Resenha
    fields = ('url','pk','dono')

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
              'pk',
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


class LivroSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Livro
    fields = ('url',
              'nome',
              'autor',
              'ano',
              'editora',
              'criado',
              'atualizado',)

class LivroDetailSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Livro
    fields = ('url',
             'nome',
             'autor',
             'ano',
             'editora',
             'criado',
             'atualizado',)

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Comentario
    fields = ('url',
              'nome',
              'email',
              'comentario',
              'resenha',
              'criado')

class ResenhaSerializer(serializers.HyperlinkedModelSerializer):
  dono = serializers.ReadOnlyField(source='dono.username')
  livro = serializers.SlugRelatedField(queryset=Livro.objects.all(),slug_field='nome')

  class Meta:
    model = Resenha
    fields = ('url',
              'livro',
              'texto',
              'dono',
              'criado',
              'atualizado',
              'nota')

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
  usuario = serializers.ReadOnlyField(source='usuario.username')

  class Meta:
    model = Avaliacao
    fields = ('url',
              'resenha',
              'estrelas',
              'usuario')