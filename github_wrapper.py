from github import Github
from .secrets import get_github_token, get_github_organization
import os

def get_github_instance() -> Github:
    return Github(get_github_token())

def get_entity(github: Github):
    if os.getenv('GITHUB_USER_MODE', 'False').lower() == 'true':
        return github.get_user()
    else:
        return github.get_organization(get_github_organization())