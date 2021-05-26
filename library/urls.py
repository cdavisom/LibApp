
from django.contrib import admin
from django.urls import path, include
from manager.views import app_home, home_remove, home_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/', include('manager.urls')),
    path('', app_home),
    path('remove/', home_remove),
    path('search/', home_search)
]
