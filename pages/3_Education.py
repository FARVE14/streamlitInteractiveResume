"""
Created By: Faisal Ahmed
Created On: 1-12-2024
"""

__author__ = "Faisal Ahmed"

import streamlit as st
from src import UserDefinedString, Icons, ReadJsonFiles

st.set_page_config(
    page_title=UserDefinedString.page_education,
    page_icon=Icons.open_book,
    layout="wide"
)

# Adding padding to the HTML page

st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

st.title(UserDefinedString.page_education)

read_json_file = st.session_state.get("json_data", ReadJsonFiles())

education_data = read_json_file.get_education_details()

for data in education_data:
    st.subheader(f"{data.degree_name}, {data.course_name}")
    st.markdown(f"{data.institute_name}, {data.from_date} - {data.end_date}")
    if data.overview:
        st.markdown(f"{data.overview}")
    if data.subjects:
        with st.expander(f"**Topics Covered:**"):
            for subject in data.subjects:
                st.markdown(f"- {subject}")
    if data.skills:
        with st.expander(f"**Skills Acquired:**"):
            for skill in data.skills:
                st.markdown(f"- {skill}")