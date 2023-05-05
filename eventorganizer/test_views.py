from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event
from django.utils import timezone


class TestHomepageView(TestCase):

    # test homepage following hello django project
    def test_homepage_url_and_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestEventInformationlView(TestCase):

    def test_event_information_url_and_template_logged_in(self):
        test_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        login = self.client.login(username='testuser', password='testpassword')
        test_event = Event.objects.create(
            name='test-event',
            owner=test_user,
            type='Fundraising',
            category='Environmental',
            summary='test',
            description='test',
            address='test',
            city='test',
            country='test',
            event_start=timezone.now(),
            event_end=timezone.now(),
            cover_image='default_image'
        )
        response = self.client.get(f'/event/{test_event.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_information.html')

    def test_event_information_redirect_not_logged_in(self):
        test_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        test_event = Event.objects.create(
            name='test-event',
            owner=test_user,
            type='Fundraising',
            category='Environmental',
            summary='test',
            description='test',
            address='test',
            city='test',
            country='test',
            event_start=timezone.now(),
            event_end=timezone.now(),
            cover_image='default_image'
        )
        response = self.client.get(f'/event/{test_event.id}')
        self.assertRedirects(response, '/accounts/login/', 302)
