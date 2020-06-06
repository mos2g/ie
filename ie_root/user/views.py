from rest_framework.generics import UpdateAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserView(ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['patch'])
    def update(self, request, *args, **kwargs):
        User.objects.filter(pk=request.user.pk).update(**request.data)
        return Response('done')

    @action(detail=False, methods=['get'])
    def me(self, request):
        user = User.objects.get(pk=request.user.pk)
        return Response(UserSerializer(user).data)
