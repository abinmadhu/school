from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('detail/',views.detail, name='detail'),
    path('button_page/',views.button_page, name='button_page'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
]
