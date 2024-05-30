from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view()),
    path('create-recipe/', views.CreateRecipe.as_view()),
    path('create-ingredient/', views.CreateIngredient.as_view()),
    path('create-rating/', views.CreateRating.as_view()),
    path('create-comment/', views.CreateComment.as_view()),
]