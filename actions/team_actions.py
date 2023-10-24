from github import GithubException
from ..github_wrapper import get_github_instance, get_entity
from ..models.team import (
    GetTeamsParams, GetTeamsResponse
)
from .. import action_store as action_store
import logging

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def get_teams(params: GetTeamsParams) -> GetTeamsResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        teams = [team.name for team in github.get_organization(params.org_name).get_teams()]
        return GetTeamsResponse(teams=teams)
    except GithubException as e:
        logger.error(f"Failed to get teams: {e}")
        raise
