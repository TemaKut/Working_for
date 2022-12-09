from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from companies.models import Company
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    ' Сераилизация модели пользователя. '

    class Meta:
        model = User
        fields = [
            'id',
            'last_login',
            'username',
            'first_name',
            'last_name',
            'date_joined',
            'logo',
            'email',
            'password',
            'role',
            'location',
            'companies',
            'is_blocked',
        ]
        depth = 1

    def validate_password(self, value: str) -> str:

        return make_password(value)


class CompanySerializer(serializers.ModelSerializer):
    ' Сериализация модели компании. '

    recruiters = serializers.SerializerMethodField(
        'get_meta_serializing_recruiters'
    )

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'logo',
            'category',
            'description',
            'location',
            'site',
            'recruiters',
            'is_blocked',
        ]
        depth = 1

    def get_meta_serializing_recruiters(self, obj):
        """ Сериализация вложенной модели пользователей. """
        user_serializer = UserSerializer
        user_serializer.Meta.depth = 0

        return user_serializer(obj.recruiters.all(), many=True).data
