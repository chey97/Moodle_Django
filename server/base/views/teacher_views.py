from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import Teacher
from ..serializers import TeacherSerializer
from ..permissions import IsTeacher, IsAdministrator


@api_view(['GET'])
@permission_classes([IsAdministrator | IsTeacher])
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdministrator])
def student_detail(request, pk):
    try:
        student = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeacherSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)