from django.conf import settings

from rest_framework import serializers

from .models import GitRepos

class GitReposSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitRepos
        fields = ['name', 'url', 'description', 'secure', 'current_version']

    def validate_description(self, value):
        if len(value) > 300:
            raise serializers.ValidationError("Description is too long. Must be less than 300 Characters.")
        return value
