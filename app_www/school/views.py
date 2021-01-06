from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Grade
from .models import Student
from .serializers import GradeSerializer
from .serializers import StudentSerializer
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    name = 'students'
    filter_fields = ['age', 'name', 'surname', 'height']
    permission_classes = [IsAuthenticated]
    search_fields = ['name', 'surname']
    ordering_fields = ['age', 'height']


class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_fields = ['subject', 'value', 'weight']
    name = 'grades'
    permission_classes = [IsAuthenticated]
    search_fields = ['subject']
    ordering_fields = ['subject', 'value', 'weight']


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    name = 'student'
    permission_classes = [IsAuthenticated]


class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    name = 'grade'
    permission_classes = [IsAuthenticated]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users'
    permission_classes = [IsAuthenticated]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user'
    permission_classes = [IsAuthenticated]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'students': reverse(StudentList.name, request=request),
                         'grades': reverse(GradeList.name, request=request),
                         'users': reverse(UserList.name, request=request)
                         })
