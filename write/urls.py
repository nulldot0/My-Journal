from django.urls import path
from . import views

urlpatterns = [
    path('', views.write),
    path('writing/', views.writing)
]
