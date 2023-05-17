from django.test import TestCase, Client
from users.models import User
from django.urls import reverse

client = Client()


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='mail@gmail.com',
            username='mail',
            password='1',

        )
        self.new_user_data = {
            "email": "malla@mail.ru",
            "username": "malla",
            "first_name": "str",
            "last_name": "ring",
            "password": "1",
            "password2": "1"
        }

    def test_user_register(self):
        url = reverse('register')
        response = client.post(url, data=self.new_user_data)
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.status_code, 400)
        self.assertEqual(response.data["email"], self.new_user_data["email"])

    def test_user_list(self):
        url = reverse('user-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.json()["results"][0]["email"], self.user.email)

    def test_user_detail(self):
        url = reverse('user-detail', kwargs={"pk": self.user.pk})
        response = client.delete(url)
        print(response)
        self.assertEqual(response.status_code, 204)
