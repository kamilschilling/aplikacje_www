from django.urls import path
from .views import GradeList
from .views import StudentList
from .views import GradeDetail
from .views import StudentDetail
from .views import ApiRoot
from .views import UserList
from .views import UserDetail

urlpatterns = [
    path('students', StudentList.as_view(), name=StudentList.name),
    path('grades', GradeList.as_view(), name=GradeList.name),
    path('grades/<int:pk>', GradeDetail.as_view(), name=GradeDetail.name),
    path('students/<int:pk>', StudentDetail.as_view(), name=StudentDetail.name),
    path('users', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>', UserDetail.as_view(), name=UserDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
]


