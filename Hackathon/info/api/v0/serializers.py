from rest_framework import serializers
from info.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta():
        model = Profile
        fields = ['Gender', 'Weight', 'Height', 'Goals', 'Activity']
