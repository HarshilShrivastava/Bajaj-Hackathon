from rest_framework import serializers
from food.models import(
    Food,
    FoodNutrition
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
        



class FoodReadSerializer(serializers.ModelSerializer):


    class Meta():
        model = FoodNutrition
        fields = '__all__'


# name=models.CharField(max_length=255)
#     description=models.TextField()
#     Food_Group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
#     Category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     AvailablityTier = models.ForeignKey(AvailablityLevel, on_delete=models.CASCADE)
#     Processing_level=models.ForeignKey(Processing,on_delete=models.CASCADE)
#     Unitconversion=models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=4)
#     Calories=models.PositiveIntegerField(null=True)
#     Lactose_Intolerance=models.BooleanField(default=False)
#     Fat=models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
#     Protein =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
#     Carbohydrate =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
#     Vitamin=models.ForeignKey(Vitamins,on_delete= models.CASCADE)
#     Sugars =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
#     Fiber =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
#     Cholesterol =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
#     Saturated_Fats =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
#     Image=models.ImageField(upload_to='Food/',null=True,blank=True)
#     Problems_Can_Solve=models.ManyToManyField(Problem)
