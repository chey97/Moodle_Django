from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from ..models import Classroom
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsAdministrator
from ..serializers import ClassroomSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def classroom_list_get(request):
    classrooms = Classroom.objects.all()
    serializer = ClassroomSerializer(classrooms, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdministrator])
def classroom_create_post(request):
    serializer = ClassroomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdministrator])
def classroom_detail(request, pk):
    try:
        classroom = Classroom.objects.get(pk=pk)
    except Classroom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)