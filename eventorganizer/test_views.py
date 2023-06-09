from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Event


class TestHomepageView(TestCase):
    # test homepage following hello django project
    def test_homepage_url_and_template(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


class TestEventInformationlView(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "tespassword"
        test_user = User.objects.create_user(
            username=self.username, password=self.password
        )
        test_event = Event.objects.create(
            name="test-event",
            owner=test_user,
            type="Fundraising",
            category="Environmental",
            summary="test",
            description="test",
            address="test",
            city="test",
            country="test",
            start_date=timezone.now(),
            start_time=timezone.now(),
            end_date=timezone.now(),
            end_time=timezone.now(),
            cover_image="default_image",
        )

    def test_event_information_url_and_template_logged_in(self):
        self.client.login(username=self.username, password=self.password)
        test_event = Event.objects.first()
        test_event.approved = True
        test_event.save()
        response = self.client.get(f"/event/{test_event.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "event_information.html")

    def test_event_information_redirect_not_logged_in(self):
        test_event = Event.objects.first()
        response = self.client.get(f"/event/{test_event.id}")
        self.assertRedirects(response, "/accounts/login/", 302)

    def test_event_information_redirect_event_not_approved(self):
        self.client.login(username=self.username, password=self.password)
        test_event = Event.objects.first()
        response = self.client.get(f"/event/{test_event.id}")
        self.assertRedirects(response, "/", 302)

    def test_event_information_redirect_event_archived(self):
        self.client.login(username=self.username, password=self.password)
        test_event = Event.objects.first()
        test_event.approved = True
        test_event.archived = True
        test_event.save()
        response = self.client.get(f"/event/{test_event.id}")
        self.assertRedirects(response, "/", 302)


class TestJoinEventView(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        test_user = User.objects.create_user(
            username=self.username, password="testpassword"
        )
        test_event = Event.objects.create(
            name="test-event",
            owner=test_user,
            type="Fundraising",
            category="Environmental",
            summary="test",
            description="test",
            address="test",
            approved=True,
            city="test",
            country="test",
            start_date=timezone.now(),
            start_time=timezone.now(),
            end_date=timezone.now(),
            end_time=timezone.now(),
            cover_image="default_image",
        )

    def test_join_event_url_and_redirect(self):
        self.client.login(username=self.username, password=self.password)
        test_event = Event.objects.first()
        response = self.client.post(f"/event/{test_event.id}/join")
        self.assertRedirects(
            response, reverse("event_information", args=[test_event.id]), 302
        )

    def test_join_event_adds_user_to_event_participants(self):
        self.client.login(username=self.username, password=self.password)
        test_event = Event.objects.first()
        user = User.objects.first()
        response = self.client.post(f"/event/{test_event.id}/join")
        self.assertEqual(test_event.participants.first(), user)

    def test_join_event_adds_event_to_user_events_list(self):
        self.client.login(username=self.username, password=self.password)
        test_event = Event.objects.first()
        user = User.objects.first()
        response = self.client.post(f"/event/{test_event.id}/join")
        self.assertEqual(user.event_participants.first(), test_event)


class TestCancelEventParticipationView(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "tespassword"
        test_user = User.objects.create_user(
            username=self.username, password=self.password
        )
        test_event = Event.objects.create(
            name="test-event",
            owner=test_user,
            type="Fundraising",
            category="Environmental",
            summary="test",
            description="test",
            address="test",
            approved=True,
            city="test",
            country="test",
            start_date=timezone.now(),
            start_time=timezone.now(),
            end_date=timezone.now(),
            end_time=timezone.now(),
            cover_image="default_image",
        )
        test_event.participants.add(test_user)
        test_event.save()

    def test_leave_event_url_and_redirect(self):
        self.client.login(username=self.username, password=self.password)
        test_event = Event.objects.first()
        response = self.client.post(f"/event/{test_event.id}/leave")
        self.assertRedirects(
            response, reverse("event_information", args=[test_event.id]), 302
        )

    def test_leave_event_removes_user_from_event_participants(self):
        self.client.login(username=self.username, password=self.password)
        test_event = Event.objects.first()
        user = User.objects.first()
        response = self.client.post(f"/event/{test_event.id}/leave")
        self.assertNotIn(user, test_event.participants.all())

    def test_leave_event_removes_event_from_user_event_list(self):
        self.client.login(username=self.username, password=self.password)
        test_event = Event.objects.first()
        user = User.objects.first()
        response = self.client.post(f"/event/{test_event.id}/leave")
        self.assertNotIn(test_event, user.event_participants.all())
