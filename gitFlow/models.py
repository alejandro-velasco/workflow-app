from django.db import models

# Git Repositories Model
class GitRepos(models.Model):
    name = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    secure = models.BooleanField(default=True)

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "url" : self.url,
            "description" : self.description,
            "secure" : self.secure
        }
