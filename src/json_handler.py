"""
Created By: Faisal Ahmed
Created On: 1-12-2024
"""

__author__ = "Faisal Ahmed"

import json
from pathlib import Path
from src.schema_handler import Introduction, ProfessionalExperience, Education


class ReadJsonFiles:
    """

    """
    def __init__(self):
        self.current_working_dir = Path().absolute()
        self.data_folder = "data"

    def get_introduction_data(self, file_name: str = "introduction.json") -> Introduction:
        """

        """
        with open(self.current_working_dir / self.data_folder / file_name, 'r') as file_data:
            return Introduction(**json.load(file_data))

    def get_professional_experience(self, file_name: str = "professional_experience.json") -> (
            list)[ProfessionalExperience]:
        """

        """
        with open(self.current_working_dir / self.data_folder / file_name, 'r') as file_data:
            return [ProfessionalExperience(**data) for data in json.load(file_data)]

    def get_education_details(self, file_name: str = "education.json") -> list[Education]:
        """

        """
        with open(self.current_working_dir / self.data_folder / file_name, 'r') as file_data:
            return [Education(**data) for data in json.load(file_data)]
