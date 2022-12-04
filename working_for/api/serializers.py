from django.contrib.auth.hashers import make_password

from rest_framework.serializers import ModelSerializer


from users.models import User


class UserSerializer(ModelSerializer):
    """ Сераилизация модели пользователя. """

    def validate_password(self, value: str) -> str:

        return make_password(value)

    class Meta:
        model = User

        exclude = [
            'groups',
            'user_permissions',
            'is_superuser',
            'is_staff',
            'is_active',
        ]

        extra_kwargs = {
            'password': {
                'required': True,
                'write_only': True,
                },
        }
