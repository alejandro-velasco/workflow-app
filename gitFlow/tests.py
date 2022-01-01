from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import GitRepos

class GitReposTestCase(TestCase):
    """
    Ensure Objects can be created
    """
    def test_git_repo_created(self):
        git_repo_obj = GitRepos.objects.create(
            name='test-case-repo',
            url='https://github.com/testcase/repo.git',
            description='A Test Case Repository',
            secure='True'
            current_version='v0.0.0'
        )
        self.assertEqual(git_repo_obj.id, 1)

class GitReposAPITests(APITestCase):
    def test_git_repo_api(self):
        """
        Ensure we can create new GitRepo object
        """
        url = reverse('git-repo-list')
        data = {
            'name': 'test',
            'url': 'http://localhost:8080/test.git',
            'description': 'test',
            'secure': False,
            'current_version': 'v0.0.0'
        }
        response_post = self.client.post(url, data, format='json')
        response_get = self.client.get(url, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(GitRepos.objects.count(), 1)
        self.assertEqual(GitRepos.objects.get().name, 'test')
