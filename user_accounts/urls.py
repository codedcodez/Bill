from django.urls import path

from . import views

app_name = 'user_accounts'

urlpatterns = [
    path('account/', views.signup, name='signup'),
]
