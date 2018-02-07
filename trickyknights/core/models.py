import random
import uuid
from django.db import models
from django.db.models.aggregates import Count
from rest_framework import serializers

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class PuzzleManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = random.randint(0, count - 1)
        return self.all()[random_index]

class Puzzle(BaseModel):
    uuid = models.UUIDField(
        default = uuid.uuid4,
        editable = False)
    init_fen = models.CharField(max_length=100, unique=True)
    move_played = models.CharField(max_length=10)
    best_move_san = models.CharField(max_length=10)
    best_move_uci = models.CharField(max_length=10)
    game_url = models.URLField(blank=True)

    objects = PuzzleManager()

    def __str__(self):
        return self.init_fen

class Game(BaseModel):
    pgn = models.TextField(max_length=5000)
    game_url = models.URLField(blank=True)

    def __str__(self):
        return self.pgn[:50]
