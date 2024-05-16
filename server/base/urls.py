from django.urls import path
from .views import student_list, student_detail, teacher_list, classroom_list, classroom_detail, subject_list

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>/', student_detail, name='student-detail'),
    path('teacher/', teacher_list, name='teacher-list'),
    path('classrooms/', classroom_list, name='classroom-list'),
    path('classrooms/<int:pk>/', classroom_detail, name='classroom-detail'),
    path('subjects/', subject_list, name='subject-list'),
]

