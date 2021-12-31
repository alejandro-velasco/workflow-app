from django.test import TestCase
from .models import GitRepos

class GitReposTestCase(TestCase):
    def test_git_repo_created(self):
        git_repo_obj = GitRepos.objects.create(
            name='test-case-repo',
            url='https://github.com/testcase/repo.git',
            description='A Test Case Repository',
            secure='True'
        )
        self.assertEqual(git_repo_obj.id, 1)
