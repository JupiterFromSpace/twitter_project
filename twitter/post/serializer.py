from rest_framework import serializers
from post.models import UserProfile,Post,Comment


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"
 


class CreatUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ("name","age","bio","email",)
 

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


