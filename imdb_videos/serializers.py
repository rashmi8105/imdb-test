# -*- coding: utf-8 -*-
from rest_framework import serializers
from imdb_videos.models import Videos, LANGUAGE_CHOICES, STYLE_CHOICES


class VideosSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    genre = serializers.CharField(required=True, max_length=100)
    popularity = serializers.CharField(required=False)
    director = serializers.CharField(required=False, default='')
    imdb_score = serializers.CharField(default='0.0')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Videos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.popularity = validated_data.get('popularity', instance.popularity)
        instance.director = validated_data.get('director', instance.director)
        instance.imdb_score = validated_data.get('imdb_score', instance.imdb_score)
        instance.save()
        return instance

    class Meta:
        model = Videos
        fields = ('id', 'name', 'genre', 'popularity', 'director', 'imdb_score')
