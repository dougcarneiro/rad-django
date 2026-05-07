from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # auth
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]