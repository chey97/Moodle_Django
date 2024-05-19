from django.urls import path
from base.views.subject_views import subject_list
from base.views.student_views import student_list, student_detail
from base.views.teacher_views import teacher_list
from base.views.classroom_views import classroom_list, classroom_detail

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>/', student_detail, name='student-detail'),
    path('teacher/', teacher_list, name='teacher-list'),
    path('classrooms/', classroom_list, name='classroom-list'),
    path('classrooms/<int:pk>/', classroom_detail, name='classroom-detail'),
    path('subjects/', subject_list, name='subject-list'),
]

