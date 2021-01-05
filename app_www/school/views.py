from rest_framework import generics
from .models import Grade
from .models import Student
from .serializers import GradeSerializer
from .serializers import StudentSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    name = 'students'


class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    name = 'grades'
