from django.urls import path

from account import views
from account.views import ProfileView, FollowView

app_name = "account"
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),

    path('<str:username>/', ProfileView.as_view(), name="profile"),
    path('follow/<str:username>/', FollowView.as_view(), name="follow")
]
