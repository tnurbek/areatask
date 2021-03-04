from rest_framework import serializers
from .models import Area


class AreaSerializer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField()

    colors = serializers.SerializerMethodField()

    def get_points(self, obj):
        return f'[{obj.longitude} {obj.latitude}]'

    def get_colors(self, obj):
        if obj.fill_type == 'CLR':
            return f'{obj.color}'
        elif obj.fill_type == 'GRD':
            return f'{obj.color1}, {obj.color2}, {obj.angle}'

    class Meta:
        model = Area
        fields = ('id', 'name', 'description', 'points', 'fill_type', 'colors', 'color', 'color1', 'color2', 'angle', 'longitude',
                  'latitude',)
        extra_kwargs = {
            'latitude': {'write_only': True},
            'longitude': {'write_only': True},
            'color': {'write_only': True},
            'color1': {'write_only': True},
            'color2': {'write_only': True},
            'angle': {'write_only': True},
        }
        # exclude = ('longitude', 'latitude',)
