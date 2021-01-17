from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('my-own-admin-login/', admin.site.urls),
    path('api/', include('pdapi.urls'))
]