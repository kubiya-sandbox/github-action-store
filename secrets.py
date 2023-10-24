import os
from . import action_store

def get_github_token():
    token = action_store.secrets.get("GITHUB_TOKEN")
    if token is None:
        raise EnvironmentError("GITHUB_TOKEN is not set in environment variables.")
    return token

def get_github_organization():
    org = action_store.secrets.get("GITHUB_ORGANIZATION")
    if org is None:
        raise EnvironmentError("GITHUB_ORGANIZATION is not set in environment variables.")
    return org