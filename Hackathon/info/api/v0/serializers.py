from rest_framework import serializers
from info.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta():
        model = Profile
        fields = ['Gender', 'Weight', 'Height', 'Goals', 'Activity','Age']

class ProfileReadSerializer(serializers.ModelSerializer):
    Username=serializers.SerializerMethodField('get_username')
    Condition=serializers.SerializerMethodField('get_Condition')
    Gender=serializers.SerializerMethodField('get_Gender')
    Activity=serializers.SerializerMethodField('get_Activity')
    Goals=serializers.SerializerMethodField('get_Goals')

    class Meta():
        model = Profile
        fields = ['Gender', 'Weight', 'Height', 'Goals', 'Activity','Age','Username','BMI','DailyCalories','BMR','Condition']

    def get_username(self,info):
        data=info.User.username
        return data
    def get_Condition(self,info):
        data=info.Condition
        if data=='1':
            return "Underweight"
        if data=='2':
            return "Normal"
        if data=='3':
            return "Overweight"
        if data=='4':
            return "Obesity"
    def get_Gender(self,info):
        data=info.Gender
        a=''
        if data=='1':
            a= "Male"
        if data=='2':
            a= "Female"
        return a
    def get_Goals(self,info):
        data=info.Goals
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
        data=info.Activity
        if data=='1':
            return "Sedentary"
        if data=='2':
            return "Lightly Active"
        if data=='3':
            return "Active"
        if data=='4':
            return "Very Active"