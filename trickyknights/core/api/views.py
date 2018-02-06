from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle

from ..models import Puzzle
from .serializers import PuzzleSerializer

class PuzzleListCreateAPIView(ListCreateAPIView):
    queryset = Puzzle.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = PuzzleSerializer
    lookup_field = 'id'

class PuzzleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Puzzle.objects.all()
    throttle_classes = (AnonRateThrottle, )
    serializer_class = PuzzleSerializer
    lookup_field = 'uuid'
