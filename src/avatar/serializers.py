from rest_framework import serializers

class HotTakeSerializer(serializers.Serializer):
    instruction = serializers.CharField(max_length=2500)
    news_article_url = serializers.URLField(max_length=400, required=False)


