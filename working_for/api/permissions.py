from rest_framework.permissions import BasePermission


class CanUpdateInfoAboutSelf(BasePermission):
    """ Допускается изменение информации о себе. """

    def has_object_permission(self, request, view, obj):

        return (
            request.method in ['PATCH', 'PUT']
            and request.user.id == obj.id
            or request.user.is_admin
        )


class AdminOrEmployeeCanCreateOrUpdateCompany(BasePermission):
    """ Админ или работодатель могут создать или изменить данные компании. """

    def has_permission(self, request, view):
        pass
