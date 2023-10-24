from typing import List

from pydantic import BaseModel

from .. import action_store as s
from ..github_wrapper import get_github_instance, get_entity


class HealthRequest(BaseModel):
    pass


class HealthResponse(BaseModel):
    params: bool
    connection: bool
    errors: List[str]


@s.kubiya_action()
def health_check(_: HealthRequest) -> HealthResponse:
    errors = List[str]
    params = _validate_params(errors)
    connection = _validate_conn(errors)
    return HealthResponse(params=params, connection=connection, errors=errors)


def _validate_conn(e: List[str]) -> bool:
    org = s.secrets.get("GITHUB_ORGANIZATION")
    try:
        c = get_entity(get_github_instance())
        return c.get_user().login != "" and c.get_organization(org).login != ""
    except Exception as e:
        e.append(f"faild to connect to github: {str(e)}")
        return False


def _validate_params(e: List[str]) -> bool:
    valid = True

    if s.secrets.get("GITHUB_TOKEN") == "":
        valid = False
        e.append("GITHUB_TOKEN is not set")

    if s.secrets.get("GITHUB_ORGANIZATION") == "":
        valid = False
        e.append("GITHUB_ORGANIZATION is not set")

    return valid
