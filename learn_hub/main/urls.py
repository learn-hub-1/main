from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('user_page/', views.user_page, name='user_page'),
    path('approve_mentor/<int:mentor_id>/', views.approve_mentor, name='approve_mentor'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_admin/', views.add_admin, name='add_admin'),
]