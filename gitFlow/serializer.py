from django.conf import settings

from rest_framework import serializers

from .models import GitRepos
from .utils.cryptography import encrypt_str

class GitReposSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitRepos
        fields = ['name', 'url', 'description', 'secure', 'current_version', 'git_user', 'git_email', 'git_pass']

    def validate_description(self, value):
        if len(value) > 300:
            raise serializers.ValidationError("Description is too long. Must be less than 300 Characters.")
        return value

    def to_internal_value(self, data):
        validated = {
            'name': data.get('name'),
            'url': data.get('url'),
            'description': data.get('description'),
            'secure': data.get('secure'),
            'current_version': data.get('current_version'),
            'git_user': data.get('git_user'),
            'git_email': data.get('git_email'),
            'git_pass': encrypt_str(data.get('git_pass'))
        }

        return validated;
