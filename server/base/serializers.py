import datetime
from rest_framework import serializers
from .models import Student, Teacher, Subject, Classroom, Administrator
from .models import UserProfile
from django.contrib.auth.models import User

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ['id', 'first_name', 'last_name', 'contact_no', 'email']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'contact_person', 'contact_no', 'email', 'date_of_birth', 'classroom']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'contact_no', 'email']
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']
        
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'name']
        

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(source='userprofile.role', write_only=True)
    contact_no = serializers.CharField(write_only=True)
    contact_no = serializers.CharField(write_only=True)
    contact_person = serializers.CharField(write_only=True, required=False)
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all(), write_only=True, required=False)


    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'role', 'contact_no', 'contact_person', 'classroom']

    def create(self, validated_data):
        role = validated_data.pop('userprofile')['role']
        contact_no = validated_data.pop('contact_no')
        contact_person = validated_data.pop('contact_person', '')
        classroom = validated_data.pop('classroom', None)
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        
        user_profile = UserProfile.objects.create(user=user, role=role)

        if role == 'student':
            Student.objects.create(
                first_name=user.first_name,
                last_name=user.last_name,
                contact_person=contact_person,
                contact_no=contact_no,  
                email=user.email,
                date_of_birth=datetime.date.today(),  
                classroom=classroom 
            )
        elif role == 'teacher':
            Teacher.objects.create(
                first_name=user.first_name,
                last_name=user.last_name,
                contact_no=contact_no,  
                email=user.email,
            )
        elif role == 'administrator':
            Administrator.objects.create(
                first_name=user.first_name,
                last_name=user.last_name,
                contact_no=contact_no,  
                email=user.email,
            )
        
        return user
