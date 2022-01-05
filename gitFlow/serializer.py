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
        validated = {}
        attributes = ['name', 'url', 'description', 'secure', 'current_version', 'git_user', 'git_email', 'git_pass']

        for attribute_name in attributes:
            if attribute_name in data.keys():
                if attribute_name == 'git_pass':
                    validated[attribute_name] = encrypt_str(data.get(attribute_name))
                else:
                    validated[attribute_name] = data.get(attribute_name)
        return validated;
