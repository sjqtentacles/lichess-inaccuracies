from rest_framework import serializers

from ..models import Puzzle

class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puzzle
        fields = [
            'uuid',
            'init_fen',
            'move_played',
            'best_move_san',
            'best_move_uci',
            'game_url'
            ]
