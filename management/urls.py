from django.urls import path
from . import views
from django.contrib.auth import views as authView

app_name = 'management'
urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('setpassword/', views.set_password, name='set_password'),
    path('viewbook/', views.book_list, name='book_list'),
    path('viewbook/detail/', views.detail, name='detail'),
    path('addbook/', views.add_book, name='add_book'),
    path('addImg/', views.add_img, name='add_img'),
]
