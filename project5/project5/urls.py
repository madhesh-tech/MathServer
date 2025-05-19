from django.contrib import admin
from django.urls import path
from app5 import views   # Import your app5 views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.power, name='power'),  # Home page will open the lamp power calculator
]
