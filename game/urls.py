from django.urls import path, include
from game import views

app_name = 'game'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name="show_category"),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page' ),
    path('category/<slug:category_name_slug>/page/', views.show_page, name="show_page"),
    path('category/page/likes/', views.likes_page, name="likes_page"),
    path('category/page/comments/', views.comments, name="comments"),
    path('category/page/wishlist/', views.wishlist, name="wishlist"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('account/', views.account, name='account'),
    path('account/delete_comment/', views.delete_comment, name='delete_comment'),
    path('account/delete_wishlist/', views.delete_wishlist, name='delete_wishlist'),
    path('logout/', views.user_logout, name='logout'),
    path('change/', views.change_password, name='change_password'),
    path('search/', views.search, name='search'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name="terms"),
]