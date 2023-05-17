from django.test import TestCase, Client
from django.urls import reverse
from blogs.models import Post, Category, Tag
from users.models import User

client = Client()


# Create your tests here.
class TestBlogs(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='python backend', )
        self.tet = Post.objects.get_current()
        self.tag = Tag.objects.create(name='Python', )
        self.user = User.objects.create(
            email='for@mail.ru',
            username='for',
            password='1'
        )
        self.post = Post.objects.create(

            title='backend',
            text='kgegslgjlkdsjglksjglk',
            category=self.category,
            tags=self.tag.pk
        )

    def test_user_list(self):
        url = reverse("post-list")

        client.login(username=self.user.username, password='1')
        response = client.get(url)
        print(response.data)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.json()["results"][0]["title"], self.post.title)
