from django.test import TestCase
from django.urls import reverse

from .forms import ContactForm

class ContactFormTest(TestCase):
    
    def test_contact_form_status_code(self):
        response = self.client.get(reverse('contact')) 
        self.assertEqual(response.status_code,200)

    def test_contact_form_uses_correct_template(self):
        response = self.client.get(reverse('contact')) 
        self.assertTemplateUsed(response,"contact.html")

    def test_contact_form_fill(self):
        form = ContactForm(data={"name":"Just Jay","email":"test@gmail.com","content":"Hello this test works"})
        self.assertEqual(form.errors, {})

    def test_contact_form_fill_name_error(self):
        form = ContactForm(data={"name":"","email":"test@gmail.com","content":"Hello this test works"})
        self.assertEqual(form.errors["name"], ["This field is required."])

    def test_contact_form_fill_email_error(self):
        form = ContactForm(data={"name":"Jawdat Tayfour","email":"testgmail.com","content":"Hello this test works"})
        self.assertEqual(form.errors["email"], ["Enter a valid email address."])

    def test_contact_form_fill_message_error(self):
        form = ContactForm(data={"name":"Jawdat Tayfour","email":"testgmail.com","content":""})
        self.assertEqual(form.errors["content"], ["This field is required."])