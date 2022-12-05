from rest_framework.permissions import BasePermission


class Can_Update_Info_About_Self(BasePermission):
    """ Допускается изменение информации о себе. """

    def has_object_permission(self, request, view, obj):

        return (
            request.method in ['PATCH', 'PUT']
            and request.user.id == obj.id
            or request.user.is_admin
        )
