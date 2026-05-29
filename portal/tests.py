from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Payment

class PortalTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_mission_page_status_code(self):
        response = self.client.get(reverse('mission'))
        self.assertEqual(response.status_code, 200)

    def test_donate_page_status_code(self):
        response = self.client.get(reverse('donate'))
        self.assertEqual(response.status_code, 200)

    def test_announcements_page_status_code(self):
        response = self.client.get(reverse('announcements'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_payment_portal_redirects_unauthenticated(self):
        response = self.client.get(reverse('payment'))
        self.assertEqual(response.status_code, 302)

    def test_payment_portal_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('payment'))
        self.assertEqual(response.status_code, 200)

    def test_create_payment(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('payment'), {
            'amount': '150.00',
            'description': 'Tuition Fee'
        })
        self.assertEqual(response.status_code, 302) # Should redirect back to payment
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.first().amount, 150.00)
