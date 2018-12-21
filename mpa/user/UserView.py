from rest_framework import viewsets, permissions, renderers
from rest_framework.response import Response
from rest_framework.decorators import action
from mpa import serializers
from mpa.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(methods = 'post', detail = 'False')
    def add_user(self, request, *args, **kwargs):
        pass

    @action(methods='get', detail='True')
    def find_user(self, request):
        get = request.GET
        user = self.get_object()

        return Response(user)
