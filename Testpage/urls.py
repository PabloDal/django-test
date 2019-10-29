from django.urls import path
from . import views

app_name = 'Testpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.register_user, name='form'),
    path('show/', views.show_users, name='show'),
]