from django.urls import path
from . import views
from .api import views as apiviews

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/puzzles/', apiviews.PuzzleListAPIView.as_view(), name='puzzle_rest_api'),
    path('api/puzzles/<uuid:uuid>', apiviews.PuzzleRetrieveAPIView.as_view(), name='puzzle_rud_api'),
]
