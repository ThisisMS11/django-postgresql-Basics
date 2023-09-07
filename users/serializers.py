from rest_framework import serializers
from users.models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class CustomUserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                # go into the custom User and check the presence of this email in all the already registerd users data and ensure that this one is unique
                queryset = CustomUser.objects.all()
            )
        ]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[
            validate_password
        ],
        style={
            "input_type":"password"
        }
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type":"password"
        }
    )

    class Meta:
        # This tells the serializer which model to use as a reference.
        model = CustomUser
        # This specifies which fields to include in the serialized data.
        fields=(
            "email",
            "password",
            "password2"
        )

    def validate(self,attrs):
        if attrs["password"]!=attrs["password2"]: 
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        return attrs
    
    def create(self,validated_data):
        user = CustomUser.objects.create_user(
            email= validated_data["email"],
        )
        # storing the encrypted password in the database because django by default tries to decrypt the user plaintest password when it is trying to authenticate the user by matching it with the already present passwords in the db.
        user.set_password(validated_data["password"])

        user.save()

        return user
