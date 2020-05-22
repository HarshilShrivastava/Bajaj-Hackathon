from django.urls import path, include
from .views import AllFoodViews,get_food
from rest_framework import routers
urlpatterns = [

    path('list-of-food/',AllFoodViews.as_view()),
    path('get-recoomended-food/',get_food,name="food data"),

]