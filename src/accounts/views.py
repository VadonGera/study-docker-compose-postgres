from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

# from serializers import GroupSerializer, UserSerializer
from accounts.serializers import GroupSerializer, UserSerializer
# from models import User
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint, позволяющий просматривать или редактировать данные пользователей.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint, позволяющий просматривать или редактировать группы.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
