from django.urls import path
from . import views



urlpatterns = [
    path('', views.film_list_create_api_view), # GET->list, POST->create
    path('<int:id>/', views.film_detail_api_view), # GET-> item, PUT->update, DELETE->delete
]