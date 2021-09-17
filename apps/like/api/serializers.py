from rest_framework import serializers
from apps .like.models import like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = like
        fields = ('id_user', 'id_product')


class LikeListSerializer(serializers.Serializer):
    class Meta:
        model = like

    def to_representation(self, instance):
        return {
            'id_user': instance['id_user'],
            'id_product': instance['id_product'],
        }
