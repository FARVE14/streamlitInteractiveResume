"""
File Name: main.py

"""

__author__ = "Faisal Ahmed"

from pathlib import Path
import streamlit as st
from src import (read_profile_data, publish_sidebar_details, publish_dashboard_details, publish_career_timeline,
                 publish_project_showcase, load_css, load_jss, publish_skills, publish_education, publish_references)

cw_path = Path().absolute()
assets_path = Path() / "assets"
image_path = assets_path / "images"
logo_path = image_path / "logo"
css_path = assets_path / "css"
js_path = assets_path / "js"
data_path = Path() / "data"



user_data =read_profile_data(
    profile_data_path= data_path / "profile_data.json",
)


if user_data is None:
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
        profile_image_path=image_path,
        logo_folder_path= logo_path,

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
    js_template=load_jss((js_path / "slider_script.js").__str__()),
    css_template=load_css((css_path / "slider_styles.css").__str__(), load=False))


with skills:
    publish_skills(user_data=user_data,
                   css_file_path= (css_path / "multi_select_styles.css").__str__())

with education:
    publish_education(user_data=user_data)

with references:
    publish_references(user_data=user_data)
