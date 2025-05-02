from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def public_home(request):
    return Response({"message": "Welcome to the public home page!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_list(request):
    return Response({"items": ["Apple", "Banana", "Cherry"]})