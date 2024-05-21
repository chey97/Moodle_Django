from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import Administrator
from ..serializers import AdministratorSerializer
from ..permissions import IsAdministrator


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsAdministrator])
def administrator_list(request):
    if request.method == 'GET':
        administrators = Administrator.objects.all()
        serializer = AdministratorSerializer(administrators, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdministratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)