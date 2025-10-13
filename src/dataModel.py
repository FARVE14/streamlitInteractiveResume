"""
File Name: 

"""

__author__ = "Faisal Ahmed"

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ProfileDataModel:
    name: str
    summary: str
    experience: int = None
    title: Optional[str] = None
    contact: dict[str, str] = field(default_factory=dict)
    key_skills: list[dict[str, str]] = field(default_factory=list)
    achievements: list[str] = field(default_factory=list)


@dataclass
class RoleDataModel:
    title: str
    from_date: str
    end_date: str
    responsibilities: list[str]

@dataclass
class ProjectDataModel:
    title: str
    description: str
    details: Optional[str] = None
    skills_used: list[str] = field(default_factory=list)

@dataclass
class PersonalProjectDataModel:
    name: str
    projects: list[ProjectDataModel] = field(default_factory=list)

@dataclass
class OrganizationDataModel:
    name: str
    from_date: str
    end_date: str
    location: str
    role: list[RoleDataModel]
    projects: list[ProjectDataModel]


@dataclass
class InstructorDataModel:
    institute_name: str
    degree_name: str
    course_name: str
    from_date: str
    end_date: str
    overview: Optional[str] = None

@dataclass
class ReferenceDataModel:
    name: str
    organization: Optional[str] = None
    contact: Optional[str] = None

@dataclass
class SkillDataModel:
    category: str
    technologies: list[str] = field(default_factory=list)

@dataclass
class UserProfileDataModel:
    profile: ProfileDataModel
    organization: list[OrganizationDataModel]
    personalProjects: PersonalProjectDataModel
    skills: list[SkillDataModel] = field(default_factory=list)
    education: list[InstructorDataModel] = field(default_factory=list)
    certificates: list[str] = field(default_factory=list)
    references: list[ReferenceDataModel] = field(default_factory=list)
