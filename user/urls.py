from django.urls import path,include
from .import views
urlpatterns = [
    path('login/',views.UserLogin.as_view(), name='user_login' ),
    path('logout/',views.user_logout, name='user_logout' ),
    path('signup/',views.UserSignup.as_view(), name='user_signup' ),
    path('accounts/profile/',views.profile, name='profile' ),
]
