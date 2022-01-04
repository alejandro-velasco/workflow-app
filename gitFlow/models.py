from django.db import models
from django.utils.timezone import now

# Git Repositories Model
class GitRepos(models.Model):
    name = models.TextField(blank=False, null=False, unique=True)
    url = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    secure = models.BooleanField(blank=False, null=False, default=True)
    current_version = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    git_user = models.TextField(blank=False, null=False)
    git_email = models.TextField(blank=False, null=False)
    git_pass = models.TextField(blank=False, null=False)

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "url" : self.url,
            "description" : self.description,
            "secure" : self.secure,
            "current_version" : self.current_version,
            "created_at" : self.created_at,
            "git_user" : self.git_user,
            "git_email" : self.git_email,
            "git_pass" : self.git_pass
        }
