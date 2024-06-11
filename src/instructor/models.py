from pydantic import BaseModel, Field
from enum import Enum

class Action(Enum):
    HOT_TAKE = "hot_take"

class NewsData(BaseModel):
    title: str
    summary: str
    sentiment: str

class Instruction(BaseModel):
    url: str = Field(None, description="The first URL extracted from the instruction.")
    action: Action = Field(..., description="The action to be taken based on the instruction.")
    instruction: str = Field(..., description="The instruction to be executed.")
    keywords: list[str] = Field(..., description="Search engine keywords to be extracted from the instruction.")
    mentioned_individuals: list[str] = Field(default_factory=list, description="List of Individuals mentioned in the instruction.")
    relevant_countries: list[str] = Field(default_factory=list, description="List of relevant countries represented as ISO 3166-1 alpha-2 codes.")
    # categories: list[str]

    def is_valid(self):
        if not self.instruction and not self.action:
            return False
        return True

class Status(BaseModel):
    status: str