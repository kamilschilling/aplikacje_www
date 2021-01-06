from django.utils.http import urlencode
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from . import views
from . models import Student


class StudentsTests(APITestCase):
    def post_student(self, _name, _surname, _height, _age, _is_login, _username, _password, _email):
        user = User.objects.create_user(_username, _email, _password)
        if _is_login:
            self.client.login(username=_username, password=_password)
        url = reverse(views.StudentList.name)
        data = {
            'name': _name,
            'surname': _surname,
            'height': _height,
            'age': _age,
            'user': user.id
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_student_without_login(self):
        response = self.post_student('Jan', 'Jankowski', '1.88', 17, False, 'test1', 'test123', 'test@test.pl')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # no login

    def test_post_student_with_login(self):
        response = self.post_student('Jan', 'Jankowski', '1.88', 17, True, 'test2', 'test123', 'test@test.pl')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # log in

    def test_student_user(self):
        response = self.post_student('Jan', 'Jankowski', '1.88', 17, True, 'test3', 'test123', 'test@test.pl')
        user = User.objects.filter(id=response.data['user'])[0]
        self.assertEqual(user.username, 'test3')
        self.assertEqual(user.email, 'test@test.pl')
        self.assertTrue(user.check_password('test123'))

    def test_count_objects(self):
        self.post_student('Jan', 'Jankowski', '1.88', 17, True, 'test4', 'test123', 'test@test.pl')
        self.post_student('Jan', 'Jankowski', '1.88', 17, True, 'test5', 'test123', 'test@test.pl')
        self.post_student('Jan', 'Jankowski', '1.88', 17, True, 'test6', 'test123', 'test@test.pl')
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 3)

    def test_filter_age_students(self):
        self.post_student('Jan', 'Jankowski', '1.88', 17, True, 'test4', 'test123', 'test@test.pl')
        self.post_student('Jan', 'Jankowski', '1.89', 17, True, 'test5', 'test123', 'test@test.pl')
        self.post_student('Jan', 'Jankowski', '1.88', 17, True, 'test6', 'test123', 'test@test.pl')
        filter_by_height = {'height': '1.88'}
        url = '{0}?{1}'.format(reverse(views.StudentList.name), urlencode(filter_by_height))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['results'][0]['height'], '1.88')

    def test_student_return_string(self):
        self.post_student('Stefan', 'Stefanowski', '1.88', 17, True, 'test4', 'test123', 'test@test.pl')
        student = Student.objects.all()[0]
        self.assertEqual(str(student), 'Stefanowski Stefan')



