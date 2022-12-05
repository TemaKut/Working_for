from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User
from .serializers import UserSerializer, UserInfoAboutMeSerializer
from .permissions import Can_Update_Info_About_Self


class UserViewSet(ModelViewSet):
    """
    Взаимодействие с пользователями:

    Пользователю доступно изменение только своих данных (Удалять нельзя)
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [Can_Update_Info_About_Self]


@api_view(['GET'])
def get_info_about_me(request):
    """ Получить информацию o себе. """
    user = get_object_or_404(User, id=request.user.id)
    serializer = UserInfoAboutMeSerializer(user)

    return Response(serializer.data)
