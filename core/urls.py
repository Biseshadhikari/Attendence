
from django.urls import path
from core import views

urlpatterns = [
    path('',views.Home,name = "home"),
    path('login/',views.signin,name = "login"),
    path('logout/',views.user_logout,name = 'logout'),
    path('create_student/', views.create_student, name='create_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('create_course/', views.create_course, name='create_course'),
    path('create_mentor/', views.create_mentor, name='create_mentor'),
    path('chiya',views.chiya)
    # path('pass/word_change_done/', views.password_change_done, name='password_change_done'),



]
