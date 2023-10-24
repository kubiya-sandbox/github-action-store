from github import GithubException
from ..github_wrapper import get_github_instance, get_entity
from ..models.issue import (
    CreateIssueParams, CreateIssueResponse,
    CloseIssueParams, CloseIssueResponse,
    GetIssueParams, GetIssueResponse
)
from .. import action_store as action_store
import logging

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def create_issue(params: CreateIssueParams) -> CreateIssueResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        issue = repo.create_issue(
            title=params.title,
            body=params.body,
        )
        return CreateIssueResponse(issue_url=issue.html_url, **issue.raw_data)
    except GithubException as e:
        logger.error(f"Failed to create issue: {e}")
        raise

@action_store.kubiya_action()
def close_issue(params: CloseIssueParams) -> CloseIssueResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        issue = repo.get_issue(number=params.issue_number)
        issue.edit(state='closed')
        return CloseIssueResponse(success=True)
    except GithubException as e:
        logger.error(f"Failed to close issue: {e}")
        raise

@action_store.kubiya_action()
def get_issue(params: GetIssueParams) -> GetIssueResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        issue = repo.get_issue(number=params.issue_number)
        return GetIssueResponse(issue_url=issue.html_url, title=issue.title, body=issue.body, state=issue.state)
    except GithubException as e:
        logger.error(f"Failed to get issue: {e}")
        raise