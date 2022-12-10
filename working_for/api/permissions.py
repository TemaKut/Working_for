from rest_framework.permissions import BasePermission, SAFE_METHODS


class CanUpdateInfoAboutSelf(BasePermission):
    """ Допускается изменение информации о себе. """

    def has_object_permission(self, request, view, obj):

        if request.method not in SAFE_METHODS:

            return request.user.id == obj.id or request.user.is_admin

        else:

            return request.method in SAFE_METHODS


class AdminOrEmployeeCanCreateOrUpdateCompany(BasePermission):
    """ Админ или работодатель могут создать или изменить данные компании. """

    def has_permission(self, request, view):
        pass
