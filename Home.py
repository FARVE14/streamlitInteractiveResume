"""
File Name: main.py

"""

__author__ = "Faisal Ahmed"

from pathlib import Path
import streamlit as st
import os
from dotenv import load_dotenv
from dataclasses import dataclass
from src import (read_profile_data, publish_sidebar_details, publish_dashboard_details, publish_career_timeline,
                 publish_project_showcase, load_css, load_jss, publish_skills, publish_education, publish_references)


load_dotenv()


@dataclass
class ProfileDataContext:
    user_name: str

    def __post_init__(self):
        cw = Path().absolute()
        assert_path = cw.joinpath("assets")
        image_folder_path = assert_path.joinpath("images")
        data_folder_path = assert_path.joinpath("data")
        self.css_folder_path = assert_path.joinpath("css")
        self.js_folder_path = assert_path.joinpath("js")
        self.logo_folder_path = image_folder_path.joinpath("logo")
        self.image_path = image_folder_path.joinpath(f"profile_{self.user_name.lower()}.png")
        self.user_data = read_profile_data(
            profile_data_path=data_folder_path.joinpath(f"profile_data_{self.user_name.lower()}.json")
        )

user_config = ProfileDataContext(user_name=os.getenv("USER_NAME", "faisalAhmed").strip().lower().
                                 replace(" ", ""))
user_data = user_config.user_data


if user_data is None:
    st.warning("Unable to process user data.")
    st.stop()

st.set_page_config(
    page_title= user_data.profile.name,
    layout="wide",
    page_icon="🤖"
)

st.title(f"🤖 {user_data.profile.name}")

st.markdown(f"### Hello, I am **{user_data.profile.name}**, a {user_data.profile.title}")


st.subheader("Profile Summary")

st.write(user_data.profile.summary)


# Show user profile and contact profiles
with st.sidebar:
    publish_sidebar_details(
        user_data=user_data,
        profile_image_path=user_config.image_path.__str__(),
        logo_folder_path= user_config.logo_folder_path,

    )


dashboard, career_timeline, project_show_case, skills, education, references = st.tabs([
    "☰ Dashboard", "🗓 Career Timeline", "📑 Project Show Case", "🛠 Skills", "🎓 Education", "🌐 References"
], width ="stretch")


with dashboard:
    publish_dashboard_details(user_data=user_data)


with career_timeline:
    publish_career_timeline(user_data=user_data)

with project_show_case:
    publish_project_showcase(
        user_data=user_data,
    js_template=load_jss((user_config.js_folder_path / "slider_script.js").__str__()),
    css_template=load_css((user_config.css_folder_path / "slider_styles.css").__str__(), load=False))


with skills:
    publish_skills(user_data=user_data,
                   css_file_path= (user_config.css_folder_path / "multi_select_styles.css").__str__())

with education:
    publish_education(user_data=user_data)

with references:
    publish_references(user_data=user_data)
