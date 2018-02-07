from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.pagination import PageNumberPagination

from ..models import Puzzle
from .serializers import PuzzleSerializer

class PuzzlePagination(PageNumberPagination):
    page_size=5
    page_size_query_param = 'page_size'
    max_page_size = 50

class PuzzleListAPIView(ListCreateAPIView):
    queryset = Puzzle.objects.all()
    pagination_class = PuzzlePagination
    # permission_classes = (IsAuthenticated, )
    serializer_class = PuzzleSerializer

class PuzzleRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Puzzle.objects.all()
    throttle_classes = (AnonRateThrottle, )
    serializer_class = PuzzleSerializer
    lookup_field = 'uuid'
