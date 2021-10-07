from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def create_sample_user(email='test@mycompany.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@ranomemail.com'
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LondonDEVAPP.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that creating user with no blank_email creates an error"""
        with self.assertRaises(ValueError):
            blank_email = ''
            get_user_model().objects.create_user(blank_email, 'test123')

    def test_create_superuser(self):
        """Test creating a superuser"""
        superuser = get_user_model().objects.create_superuser(
            'test123@myemail.com',
            'test123'
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=create_sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)
