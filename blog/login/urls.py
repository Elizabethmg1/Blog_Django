from django.urls import path
from login import views
from django.contrib.auth.views import LogoutView

app_name = 'login'

urlpatterns = [
    path('', views.login1, name='login'),
    path('error/', views.passornameincorrect, name='passornameincorrect'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
]