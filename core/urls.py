
from django.urls import path
from core import views

urlpatterns = [
    path('',views.Home,name = "home"),
    path('login/',views.signin,name = "login"),
    path('logout/',views.user_logout,name = 'logout'),
     path("qr/", views.generate_qr, name="generate_qr"),  # Generates a static QR code
    path("scan/", views.scan_qr, name="scan_qr"),
    path('password_change/', views.custom_password_change, name='password_change'),


    # path('pass/word_change_done/', views.password_change_done, name='password_change_done'),



]
