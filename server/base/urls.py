from django.urls import path, include
from base.views.subject_views import subject_list_get, subject_create_post, subject_manage
from base.views.administrator_view import administrator_list
from base.views.student_views import student_list_get, student_detail
from base.views.teacher_views import teacher_list
from base.views.classroom_views import classroom_list_get, classroom_create_post, classroom_detail
from .views.create_user import CreateUserView, ListUsersView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('administrator/', administrator_list, name='administrator-list'),
    path('students/', student_list_get, name='student-list-get'),
    path('students/<int:pk>/', student_detail, name='student-detail'),
    path('teacher/', teacher_list, name='teacher-list'),
    path('classrooms/', classroom_list_get, name='classroom-list'),
    path('classrooms/create/', classroom_create_post, name='classroom-list-post'),
    path('classrooms/<int:pk>/', classroom_detail, name='classroom-detail'),
    path('subjects/', subject_list_get, name='subject-list'),
    path('subject/create/', subject_create_post, name='subject-create'),
    path('subject/manage/<int:pk>/', subject_manage, name='subject-manage'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('create-user/', CreateUserView.as_view(), name='create_user'),
    path('list-users/', ListUsersView.as_view(), name='list_users'), 
    path('api-auth/', include("rest_framework.urls")),
]

