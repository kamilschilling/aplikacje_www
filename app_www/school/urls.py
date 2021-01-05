from django.urls import path
from .views import GradeList
from .views import StudentList

urlpatterns = [
    path('students', StudentList.as_view(), name=StudentList.name),
    path('grades', GradeList.as_view(), name=GradeList.name),
]


