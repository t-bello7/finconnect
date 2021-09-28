from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .views import LoginView, RegistrationView, LogoutView, ProfileView
from faker import Faker
# Create your tests here.

User = get_user_model()

class UserTests(TestCase):
    def test_create_user(self):
        user = User.objects.create(full_name='Test User',email='abc@xyz.com', password='123password@')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'abc@xyz.com')
        self.assertEqual(user.full_name, 'Test User')
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(email='admin@xyz.com', password='123password@')
        self.assertEqual(admin_user.email, 'admin@xyz.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

            
    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user( email ='', password='123password@'))
        self.assertRaisesMessage(ValueError, 'The given username must be set')
     
    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(email='', password='123password@')

class TestSetUp(TestCase):
    def setUp(self):
        self.register_url = reverse('signup')
        self.register_response = self.client.get(self.register_url)
        self.login_url = reverse('login')
        self.login_response = self.client.get(self.login_url)
        self.fake = Faker()

        self.user_data={
            'email':self.fake.email(),
            'password':self.fake.email().split('@')[0], 
        }
        return super().setUp()



class RegistrationTests(TestSetUp):
    def test_signup_template(self):
        self.assertEqual(self.register_response.status_code, 200)
        self.assertTemplateUsed(self.response, 'authentication/signup.html')
        self.assertContains(self.response, 'Create an account!')
        self.assertNoContains(self.response, 'Hey i should not be here')

    def test_signup_form(self):
        new_user = User.objects.create_user(self.full_name, self.email, self.password)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, self.username)
        self.assertEqual(User.objects.all()[0].email, self.email)
    
    def test_signup_view(self):
        view = resolve('auth/signup')
        self.assertEqual(
            view.func.__name__,
            RegistrationView.as_view().__name__
        )

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_with_data(self):
        res = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['fullname'], self.user_data['username'])
        self.assertEqual(res.status_code, 201)


class LoginTests(TestSetUp):
    def test_login_template(self):
        pass

    def test_login_form(self):
        pass

    def test_login_view(self):
        pass
    
    def test_user_cannot_login_with_no_data(self):
        pass

    def test_user_can_login_with_data(self):
        pass

