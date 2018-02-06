from django.urls import path
from .api import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/puzzles/', views.PuzzleListCreateAPIView.as_view(), name='puzzle_rest_api'),
    path('api/puzzles/<uuid:uuid>', views.PuzzleRetrieveUpdateDestroyAPIView.as_view(), name='puzzle_rud_api'),

]
