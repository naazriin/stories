from django.test import TestCase
from django.urls import reverse_lazy
from core.views import ContactView

class ContactView(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    

    def test_contact_url(self):
        contact_url = '/en/contact'
        url = reverse_lazy('core:contact')
        self.assertEqual(contact_url, url)

    def test_contact_status_code(self):
        response = self.client.get(reverse_lazy('core:contact'))
        self.assertEqual(response.status_code,200)

    def test_contact_template(self):
        response= self.client.get(reverse_lazy('core:contact'))
        self.assertTemplateUsed(response, 'contact.html')

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()