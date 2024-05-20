from django.contrib import admin
from .models import Student,Subject,Teacher,Classroom,Administrator

# Register your models here.
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Administrator)