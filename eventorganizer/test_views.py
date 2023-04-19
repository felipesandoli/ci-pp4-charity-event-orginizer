from django.test import TestCase


class TestViews(TestCase):

    # test homepage following hello django project
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
