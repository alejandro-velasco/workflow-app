from django.db import models
from django.utils import timezone

# Git Repositories Model
class GitRepos(models.Model):
    name = models.TextField(blank=False, null=False, unique=True)
    url = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    secure = models.BooleanField(default=True)
    current_version = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now())

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "url" : self.url,
            "description" : self.description,
            "secure" : self.secure,
            "current_version" : self.current_version,
            "created_at" : self.created_at
        }
