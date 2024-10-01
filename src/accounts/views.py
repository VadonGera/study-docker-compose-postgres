from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from accounts.serializers import GroupSerializer, UserSerializer

User = get_user_model()


class IsAdminOrSuperuser(permissions.BasePermission):
    """
    Разрешение, позволяющее доступ только администраторам и суперпользователям.
    """

    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_staff or request.user.is_superuser))
        # return bool(request.user and request.user.is_superuser)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint, позволяющий просматривать или редактировать данные пользователей.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSuperuser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint, позволяющий просматривать или редактировать группы.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSuperuser]
