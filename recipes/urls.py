from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view()),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view()),
    path('ratings/<int:pk>/', views.RatingDetail.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]