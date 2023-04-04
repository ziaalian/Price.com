from django.test import TestCase
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token
from .views import registerUser, loginUser, logoutUser, changePassword, resetPassword
# Create your tests here.

#create test for account views

class AccountTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register_user')
        self.login_url = reverse('login_user')
        self.logout_url = reverse('logout_user')
        self.change_url = reverse('change_password')
        self.reset_url = reverse('reset_password')
        self.user_data = {
            'username': 'testuser',
            'email': 'test@test.com',    
            'password': 'testpassword',
            'is_vendor': False,
            'is_customer': True,
        }
            
        