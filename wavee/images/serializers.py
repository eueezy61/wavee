from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
        )


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = (
            'id',
            'creator',
        )


class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'creator',
        )
    