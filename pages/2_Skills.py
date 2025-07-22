"""
Created By: Faisal Ahmed
Created On: 1-12-2024
"""

__author__ = "Faisal Ahmed"

import streamlit as st
from src import UserDefinedString, Icons, ReadJsonFiles

st.set_page_config(
    page_title=f"{UserDefinedString.user_name} | {UserDefinedString.page_skills}",
    page_icon=Icons.star,
    layout="wide"
)

# Adding padding to the HTML page

st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

st.title(UserDefinedString.page_skills)

read_json_file = st.session_state.get("json_data", ReadJsonFiles())
experience_data = read_json_file.get_professional_experience()

list_of_skills = [skill.strip() for data in experience_data for role in data.roles for skill in role.skills.split(",")]
list_of_skills = sorted(list(set(list_of_skills)))
selected_skill = st.sidebar.multiselect("Skill", list_of_skills)

for companies in experience_data:
    for roles in companies.roles:
        if any(skill in roles.skills for skill in selected_skill) or len(selected_skill) == 0:
            st.subheader(f"{roles.role_name} - {companies.company}")
            with st.expander("Skills Used:"):
                for skill in sorted(roles.skills.split(",")):
                    st.markdown(f"- {skill}")
