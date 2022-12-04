from rest_framework.permissions import BasePermission, SAFE_METHODS


class Is_Admin_Or_Read_Only(BasePermission):
    """ Допуск на создание/изменение контента только у администратора. """

    def has_permission(self, request, view):

        return (
            True if request.method in SAFE_METHODS
            else request.user.is_admin
        )

    def has_object_permission(self, request, view, obj):

        return (
            True if request.method in SAFE_METHODS
            else request.user.is_admin
        )


class Can_Update_Info_About_Self(BasePermission):
    """ Допускается изменение информации о себе. """

    def has_object_permission(self, request, view, obj):

        return (
            request.method in ['PATCH', 'PUT']
            and request.user.id == obj.id
        )
