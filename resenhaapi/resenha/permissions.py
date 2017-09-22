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