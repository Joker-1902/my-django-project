from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BlogPost


class BlogAPITest(APITestCase):
    def setUp(self):
        BlogPost.objects.create(title='Test #1', content='New content for Test #1')
        BlogPost.objects.create(title='Test #2', content='New contents for Test #2')
    def test_get_blog_post_list(self):
        url = reverse('blogpost-create-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test #1')



