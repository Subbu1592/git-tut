
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' #this allows us to serialize the field which we want
        #testing
        # exclude = ['id','name']  #here i can exclude id and name remaining fields will be serialized
        # fields = '__all__'  #here i can serialize all the fields which are available in my Student model