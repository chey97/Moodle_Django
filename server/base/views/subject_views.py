from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from ..models import Subject
from ..serializers import SubjectSerializer

    
@api_view(['GET', 'POST'])
def subject_list(request):
    if request.method == 'GET':
        teachers = Subject.objects.all()
        serializer = SubjectSerializer(teachers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    