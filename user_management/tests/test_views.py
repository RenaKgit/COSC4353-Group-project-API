from django.test import Client, TestCase
from django.urls import reverse

class TestUserProfileCreate(TestCase):
    def setup(self):
        self.client = Client()

    #Best Case
    def testing_view(self):
        test_data={
            "full_name": "kv",
            "address_1": "123 left st",
            "address_2": "",
            "city": "Houston",
            "state": "tx",
            "zip_num": "77003",
            "username": "user1",
            "password": "123pass"
        }
        response = self.client.post(reverse('create-user'), test_data)
        self.assertEqual(response.status_code, 201)

    #tests for missing fields
    def test_view_error(self):
        test_data={
            "full_name": "",
            "address_1": "123 left st",
            "address_2": "",
            "city": "Houston",
            "state": "tx",
            "zip_num": "77003",
            "username": "",
            "password": ""
        }
        response = self.client.post(reverse('create-user'), test_data)
        self.assertEqual(response.status_code, 400)

        