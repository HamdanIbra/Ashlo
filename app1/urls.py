from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('login', views.login),
    path('login_form', views.login_form),
    path('register', views.register),
    path('registration', views.registration),
    path('boys',views.boys),
    path('girls', views.girls),
    path('view',views.view_cloth)

]