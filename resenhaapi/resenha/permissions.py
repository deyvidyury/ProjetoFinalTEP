from rest_framework.permissions import *

class UsuarioOuSomenteLeitura(BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		else:
			return obj == request.user

class DonoResenhaOuSomenteLeitura(BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		else:
			return obj.dono.user == request.user

"""
REGRAS
	Comentarios
		Para comentar, usuario tem que logar
		Dono do comentario ou da resenha podem deletar comentario
		Dono do comentario pode editar comentario

	Avaliacao
		Para avaliar, usuario precisar estar logado
		Usuario so pode avaliar uma unica vez uma resenha
"""