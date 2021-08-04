from django.urls import path
from game import views

app_name = 'game'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name="show_category"),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page' ),
    path('category/<slug:category_name_slug>/page/', views.show_page, name="show_page"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('account/', views.account, name='account'),
    path('logout/', views.user_logout, name='logout'),
    path('change/', views.change_password, name='change_password'),
    path('search/', views.search, name='search'),
]