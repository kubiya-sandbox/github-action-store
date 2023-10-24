from pydantic import BaseModel
from typing import List

class GetTeamsParams(BaseModel):
    org_name: str

class GetTeamsResponse(BaseModel):
    teams: List[str]
