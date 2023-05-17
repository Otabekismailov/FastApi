from django.urls import path, re_path, include
from .views import RegistrationView, LoginView, LogoutView, ChangePasswordView, UserListApi, FacebookLogin, GoogleLogin, \
    ProfDetail

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('userlist/', UserListApi.as_view(), name='user-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user-detail/<int:pk>/', ProfDetail.as_view(), name='user-detail'),
    # path('facebook-login/', FacebookLogin.as_view(), name='facebook-login'),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login')

]
