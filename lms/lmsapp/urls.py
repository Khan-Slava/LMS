from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('superAdminPage', views.superAdminPage, name='superAdminPage'),
    path('about', views.about, name='about'),
    path('course', views.course, name='course'),
    path('price', views.price, name='price'),
    path('addCourse', views.addCourse, name='Add Course')
]