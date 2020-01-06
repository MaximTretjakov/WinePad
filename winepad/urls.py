from django.contrib import admin
from django.urls import path

from depend_form import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DependForm.as_view(), name='depend_form')
]
