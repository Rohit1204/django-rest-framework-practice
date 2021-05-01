from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Hero
from .serializers import HeroSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, Rohit!'}
        return Response(content)

class HeroViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer       