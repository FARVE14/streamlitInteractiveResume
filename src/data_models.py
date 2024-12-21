"""
Created By: Faisal Ahmed
Created On: 1-12-2024
"""

from pydantic import BaseModel


class ExperienceRole(BaseModel):
    role: str
    start_date: str
    end_date: str
    skills: list[str]


class Companies(BaseModel):
    name: str
    roles: list[ExperienceRole]
