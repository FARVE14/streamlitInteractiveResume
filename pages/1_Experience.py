"""
Created By: Faisal Ahmed
Created On: 1-12-2024
"""

__author__ = "Faisal Ahmed"

import streamlit as st
from src import UserDefinedString, Icons, ReadJsonFiles

st.set_page_config(
    page_title=UserDefinedString.page_experience,
    page_icon=Icons.smiley_blush,
    layout="wide"
)

# Adding padding to the HTML page

st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

st.title(UserDefinedString.page_experience)

read_json_file = st.session_state.get("json_data", ReadJsonFiles())
experience_data = read_json_file.get_professional_experience()

list_of_companies = [data.company for data in experience_data]

selected_company = st.sidebar.multiselect("Company Name", list_of_companies)

for data in experience_data:
    if data.company in selected_company or (not selected_company):
        st.subheader(data.company)
        for role in data.roles:
            with st.expander(f"Role: {role.role_name} ( {role.from_date} - {role.end_date} )"):
                st.write("**Responsibilities**")
                st.write(role.responsibilities)
                st.write("**Skills Used**")
                st.write(role.skills)
                st.write("**Domain**")
                st.write(role.domain)
