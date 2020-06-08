from rest_framework import serializers
from food.models import(
    Food
)
class FoodSerializer(serializers.ModelSerializer):
    #photo_url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)


    class Meta():
        model = Food
        fields = ['name','Calories','Fat','Protein','Carbohydrate','Image','id']
    def get_photo_url():
        request = self.context.get('request')
        photo_url = Food.Image.url
        return request.build_absolute_uri(photo_url)
        


