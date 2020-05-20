from django.urls import path, include
from .views import AllFoodViews
from rest_framework import routers
urlpatterns = [

path('list-of-food/',AllFoodViews.as_view()),
]