from django.urls import path
from .views import registerUser, loginUser, logoutUser, changePassword, resetPassword

urlpatterns = [
    path('register/', registerUser.as_view(), name='register_user'),
    path('login/', loginUser.as_view(), name='login_user'),
    path('logout/', logoutUser.as_view(), name='logout_user'),
    path('change/', changePassword.as_view(), name='change_password'),
    path('reset/', resetPassword.as_view(), name='reset_password'),
]