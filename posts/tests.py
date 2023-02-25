from django.test import TestCase , Client
from django.urls import reverse

class HelloTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("hello-view"))
        expected_data = "<h1>Hello<h1>"
        expected_header = "Alex"

        self.assertEqual(response.content.decode(), expected_data)
        self.assertEqual(response.status_code, 300)
        self.assertEqual(response.headers["names"], expected_header)
    
    def test_get_index(self):
        response_get = self.client.get(reverse("index-page"))
        response_post = self.client.post(reverse("index-page"))

        expected_get = "Главная страница"
        expected_post = "Не тот метод запроса"

        self.assertEqual(response_get.status_code ,200)
        self.assertEqual(response_post.status_code , 200)
        self.assertEqual(response_get.content.decode(), expected_get)
        self.assertEqual(response_post.content.decode(), expected_post)

    def test_get_info(self):
        response_get_info = self.client.get(reverse("endpoint-info"))

        expect_info = "info"

        self.assertEqual(response_get_info.content.decode(),expect_info)
        self.assertEqual(response_get_info.status_code,200)
        
    def test_get_help(self):
        response_get_help = self.client.get(reverse("get-help"))

        expected_help ="help"

        self.assertEqual(response_get_help.content.decode(), expected_help)
        self.assertEqual(response_get_help.status_code,200)