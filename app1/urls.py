from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('login', views.login),
    path('login_form', views.login_form),
    path('register', views.register),
    path('registration/', views.registration),
    path('girls', views.girls),
    path('view/<id>',views.view_cloth),
    path('checkout', views.checkout),
    path('admin', views.admin),
    path('create_cloth',views.create_cloth),
    path('add_to_cart/<id>', views.add_to_cart),
    path('cart',views.cart),
    path('submit_order', views.submit_order),
    path('order_success',views.order_success),
    path('delete_users',views.delete_users),
    path('edit/<int:id>',views.edit_quantity),
    path('delete/<int:id>',views.delete),
    path('logout',views.logout),
]