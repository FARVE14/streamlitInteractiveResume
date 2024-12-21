"""
Created By: Faisal Ahmed
Created On: 1-12-2024
"""

__author__ = "Faisal Ahmed"

from pydantic import BaseModel


class RoleSchema(BaseModel):
    role_name: str
    responsibilities: str
    skills: str
    from_date: str = ""
    end_date: str = ""
    domain: str = ""


class Introduction(BaseModel):
    linkedin: str
    gmail: str
    introduction: str
    key_skills: dict


class ProfessionalExperience(BaseModel):
    company: str
    location: str
    from_date: str
    end_date: str
    roles: list[RoleSchema]


class Education(BaseModel):
    institute_name: str
    degree_name: str
    course_name: str
    overview: str | None
    from_date: str
    end_date: str
    skills: list[str] | None
    subjects: list[str] | None
