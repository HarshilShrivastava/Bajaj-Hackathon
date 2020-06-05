from rest_framework import serializers
from info.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta():
        model = Profile
        fields = ['gender', 'weight', 'height', 'goals', 'activity','age']

class ProfileReadSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField('get_username')
    condition=serializers.SerializerMethodField('get_Condition')
    gender=serializers.SerializerMethodField('get_Gender')
    activity=serializers.SerializerMethodField('get_Activity')
    goals=serializers.SerializerMethodField('get_Goals')

    class Meta():
        model = Profile
        fields = ['gender', 'weight', 'height', 'goals', 'activity','age','username','bmi','dailyCalories','bmr','condition']

    def get_username(self,info):
        data=info.User.username
        return data
    def get_Condition(self,info):
        data=info.condition
        if data=='1':
            return "Underweight"
        if data=='2':
            return "Normal"
        if data=='3':
            return "Overweight"
        if data=='4':
            return "Obesity"
    def get_Gender(self,info):
        data=info.gender
        a=''
        if data=='1':
            a= "Male"
        if data=='2':
            a= "Female"
        return a
    def get_Goals(self,info):
        data=info.goals
        a=''
        if data=='1':
            a= "Extreme Loose Weight"
        if data=='2':
            a= "Minor Loose Weight"
        if data=='3':
            a= "Maintain Weight"
        if data=='4':
            a= "Weight gain"        
        if data=='5':
            a= "Extreme Weight gain"
        return a
    def get_Activity(self,info):
        data=info.activity
        if data=='1':
            return "Sedentary"
        if data=='2':
            return "Lightly Active"
        if data=='3':
            return "Active"
        if data=='4':
            return "Very Active"