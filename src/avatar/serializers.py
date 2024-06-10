from rest_framework import serializers

class HotTakeSerializer(serializers.Serializer):
    instruction = serializers.CharField(max_length=2500)


