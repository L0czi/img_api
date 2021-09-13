from rest_framework import serializers
from .models import Image
from sorl.thumbnail import get_thumbnail

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class BasicImageSerializer(serializers.ModelSerializer):
    image_200 = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('id','image_200',)
    
    def get_image_200(self, obj,):
        request = self.context.get('request')
        image_200 = get_thumbnail(obj.image, '200x200', crop='center', quality=99).url
        return request.build_absolute_uri(image_200)


class PremiumImageSerializer(BasicImageSerializer, serializers.ModelSerializer):
    image_400 = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('id','image','image_200','image_400')
    
    def get_image_400(self, obj,):
        request = self.context.get('request')
        image_400 = get_thumbnail(obj.image, '400x400', crop='center', quality=99).url
        return request.build_absolute_uri(image_400)




