from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.books.urls')),
    path('acount/', include('apps.acount.urls')),
]
