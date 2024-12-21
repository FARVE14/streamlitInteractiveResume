"""
Created By: Faisal Ahmed
Created On: 1-12-2024
"""

__author__ = "Faisal Ahmed"

import streamlit as st
from streamlit_extras.app_logo import add_logo
from src import UserDefinedString, Icons, ReadJsonFiles, img_to_html


st.set_page_config(
    page_title=UserDefinedString.page_title,
    page_icon=Icons.open_book,
    layout="wide"
)

read_json_file = ReadJsonFiles()
st.session_state["json_data"] = read_json_file

introduction_data = read_json_file.get_introduction_data()


# Adding padding to the HTML page

st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

add_logo(r"assets\faisalAhmed.png", height=275)

st.sidebar.subheader("Contact")


st.sidebar.markdown(f"""
<a href={introduction_data.linkedin}>{img_to_html(img_path="assets/LinkedIn.png")}
""", unsafe_allow_html=True)

st.sidebar.markdown(f"""
<a href={introduction_data.gmail}>{img_to_html(img_path="assets/gmail.png")}
""", unsafe_allow_html=True)

st.subheader("Professional Summary")

st.write(f"{read_json_file.get_introduction_data().introduction}")

st.subheader("Key Skills & Expertise:")

for skills in introduction_data.key_skills.keys():
    st.markdown(f'''
    - **{skills}**: {introduction_data.key_skills.get(skills, None)}
    ''')

st.subheader("Professional Experience:")

for experience in read_json_file.get_professional_experience():

    st.markdown(f'''
    **{experience.company}, {experience.location} -- ({experience.from_date} - {experience.end_date})**
''')
    for role in experience.roles:
        st.write(f'''
        - {role.role_name}
''')

st.subheader("Education:")

for education_data in read_json_file.get_education_details():
    st.markdown(f'''
    - **{education_data.degree_name}: {education_data.course_name}**
    
        {education_data.institute_name}, {education_data.from_date} - {education_data.end_date}
''')

