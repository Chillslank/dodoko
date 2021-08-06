from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from game import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('game/', include('game.urls')),
    path('admin/', admin.site.urls),
    #third-party login
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

