from rest_framework import serializers
from .models import Image
from sorl.thumbnail import get_thumbnail


class DisplayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "id",
            "image",
        )


class UploadImageSerializer(serializers.ModelSerializer):
    thumbnail_200 = serializers.SerializerMethodField()
    thumbnail_400 = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ("id", "image", "thumbnail_200", "thumbnail_400")

    def get_thumbnail_200(
        self,
        obj,
    ):
        request = self.context.get("request")
        thumbnail_200 = get_thumbnail(
            obj.image, "200x200", crop="center", quality=99
        ).url
        return request.build_absolute_uri(thumbnail_200)

    def get_thumbnail_400(
        self,
        obj,
    ):
        request = self.context.get("request")
        thumbnail_400 = get_thumbnail(
            obj.image, "400x400", crop="center", quality=99
        ).url
        return request.build_absolute_uri(thumbnail_400)
