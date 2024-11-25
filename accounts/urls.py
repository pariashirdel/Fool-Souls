from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.RegisterView.as_view(), name='sign_up'),
    path('login/', views.foolsoulsLoginView.as_view(), name='login'),
    path('profile/', views.Profile, name= 'profile'),
    path('profileupdate/', views.ProfileUpdate, name= 'profileupdate'),
    path('changepassword/', views.ChangePasswordView.as_view(), name='changepassword'),
    path('logout/', views.logout_view , name='logout'),
]