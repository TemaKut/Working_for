from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import User
from companies.models import Company

from . import serializers
from .permissions import Can_Update_Info_About_Self


class UserViewSet(ModelViewSet):
    """ Взаимодействие с пользователями. """

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [Can_Update_Info_About_Self]

    @action(methods=['GET'], detail=False, url_path='me', url_name='me')
    def get_info_about_me(self, request):
        """ Получить информацию o себе. """
        user = get_object_or_404(User, id=request.user.id)
        serializer = serializers.UserSerializer(user)

        return Response(serializer.data)


class CompanyViewSet(ModelViewSet):
    """ Взаимодействие с компаниями. """
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [IsAuthenticated]
