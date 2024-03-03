from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_user, name='logout'),
]
