from django.urls import path

from . import views

app_name = 'billsites'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('terms-of-use/', views.TermsView.as_view(), name='terms'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.TestView.as_view(), name='test')
]
