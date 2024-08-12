from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Mount, Coords, User
from .serializers import MountSerializer

class MountApiTestCase(APITestCase):

    def setUp(self):
        user_1 = User.objects.create(email='Test_1', phone=1111, fam='Test_1', name='Test_1', otc='Test_1')
        user_2 = User.objects.create(email='Test_2', phone=2222, fam='Test_2', name='Test_2', otc='Test_2')
        coords_1 = Coords.objects.create(latitude=5.0002, longitude=5.0002, height=100)
        coords_2 = Coords.objects.create(latitude=5.0022, longitude=5.0022, height=200)
        self.mount_1 = Mount.objects.create(user=user_1, beauty_title='beauty_title_1', title="title_1",
                                       other_titles='other_titles_1', coords=coords_1)
        self.mount_2 = Mount.objects.create(user=user_2, beauty_title='beauty_title_2', title="title_2",
                                       other_titles='other_titles_2', coords=coords_2)
    def test_get_list(self):
        url = reverse('mount-list')
        response = self.client.get(url)
        serializer_data = MountSerializer([self.mount_1, self.mount_2], many=True).data
        self.assertEqual(serializer_data, response.data['results'])
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('mount-detail', args=(self.mount_1.id,))
        response = self.client.get(url)
        serializer_data = MountSerializer(self.mount_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

class MountSerializerTestCase(TestCase):
    def setUp(self):
        user_1 = User.objects.create(email='Test_1', phone=1111, fam='Test_1', name='Test_1', otc='Test_1')
        user_2 = User.objects.create(email='Test_2', phone=2222, fam='Test_2', name='Test_2', otc='Test_2')
        coords_1 = Coords.objects.create(latitude=5.0002, longitude=5.0002, height=100)
        coords_2 = Coords.objects.create(latitude=5.0022, longitude=5.0022, height=200)
        self.mount_1 = Mount.objects.create(user=user_1, beauty_title='beauty_title_1', title="title_1",
                                       other_titles='other_titles_1',
                                       coords=coords_1)
        self.mount_2 = Mount.objects.create(user=user_2, beauty_title='beauty_title_2', title="title_2",
                                       other_titles='other_titles_2',
                                       coords=coords_2)

    def test_check(self):
        serializer_data = MountSerializer([self.mount_1, self.mount_2], many=True).data
        expected_data = [
            {
                'id': 1,
                'user': 'user_1',
                'beauty_title': 'beauty_title_1',
                'title': 'title_1',
                'other_titles': 'other_titles_1',
                'coords': 'coords_1'

            },
            {
                'id': 2,
                'user': 'user_2',
                'beauty_title': 'beauty_title_2',
                'title': 'title_2',
                'other_titles': 'other_titles_2',
                'coords': 'coords_2'

            }
        ]
        self.assertEqual(serializer_data, expected_data)

