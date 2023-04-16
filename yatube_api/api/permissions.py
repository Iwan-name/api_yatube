from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user


class IsComment(BasePermission):
    def has_object_permission(self, request, view, obj):
        if 'Authorization' not in request.headers:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if request.user != obj.author:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class IsCreateGroup(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['POST']:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
