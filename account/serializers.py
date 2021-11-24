from django.conf import settings
from rest_framework import serializers
from . import models


class SkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ['id', 'title']


class SkillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ['id', 'title', 'master', 'proficient', 'learning', 'future', 'skill_slug']


class UserSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField(read_only=True)
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_skills(self, obj):
        skills = obj.skills.all()
        return SkillListSerializer(skills, many=True).data

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = models.UserModel
        fields = ['id', 'uiid', 'email', 'image_url', 'first_name', 'middle_name', 'last_name','current_role', 'skills']


class AllUserSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField(read_only=True)
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_skills(self, obj):
        skills = obj.skills.all()
        return SkillListSerializer(skills, many=True).data

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = models.UserModel
        fields = ['id', 'uiid',  'image_url', 'first_name', 'middle_name', 'current_role', 'last_name', 'skills']
