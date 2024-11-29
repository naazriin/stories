from django.test import TestCase
from core.models import Contact



class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = {
            'name': 'John',
            'email': 'john@example.com',
            'subject': 'hi',
            'message': 'hello'
        }
        cls.contact = Contact.objects.create(**cls.data)
        return super().setUpClass()
    
    def test_contact(self):
        data = Contact.objects.get(id=1)
        self.assertEqual(data, self.contact)


    @classmethod
    def tearDownClass(cls) -> None:
        pass