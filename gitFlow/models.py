from django.db import models

class GitRepos(models.Model):
    name = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    secure = models.BooleanField(default=True)
    
