from django.contrib.auth.hashers import make_password

from rest_framework.serializers import ModelSerializer


from users.models import User


class UserSerializer(ModelSerializer):
    """ Сераилизация модели пользователя. """

    def validate_password(self, value: str) -> str:

        return make_password(value)

    class Meta:
        model = User
        fields = [
            "id",
            "last_login",
            "username",
            "first_name",
            "last_name",
            "date_joined",
            "logo",
            "email",
            "password",
            "role",
            "location",
            "companies",
            "is_blocked",
        ]
        depth = 1
        extra_kwargs = {
            'password': {
                'write_only': True,
                },
        }


class UserInfoAboutMeSerializer(ModelSerializer):
    """ Показать информацию о себе. """

    class Meta:
        model = User
        fields = [
            "id",
            "last_login",
            "username",
            "first_name",
            "last_name",
            "date_joined",
            "logo",
            "email",
            "password",
            "role",
            "location",
            "companies",
            "is_blocked",
        ]
        depth = 1
