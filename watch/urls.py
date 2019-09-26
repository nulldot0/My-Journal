from django.urls import path
from . import views

urlpatterns = [
	path('', views.watch),
	path('json', views.jsons)
]