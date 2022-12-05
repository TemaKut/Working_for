from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from users.models import User
from .serializers import UserSerializer
from .permissions import Can_Update_Info_About_Self


class UserViewSet(
                mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet,
        ):
    """
    Взаимодействие с пользователями:

    Пользователю доступно изменение только своих данных (Удалять нельзя)
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        Can_Update_Info_About_Self,
    ]
