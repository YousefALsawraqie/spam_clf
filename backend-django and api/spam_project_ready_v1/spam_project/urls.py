# project-level urls.py content
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spam_app.urls')),  # ربط URLs مع التطبيق
    path('show_api/', include('spam_app.urls'))
]