"""
Created By: Faisal Ahmed
Created On: 1-12-2024
"""

__author__ = "Faisal Ahmed"

import streamlit as st
from src import UserDefinedString, Icons

st.set_page_config(
    page_title=UserDefinedString.page_education,
    page_icon=Icons.open_book,
    layout="wide"
)

# Adding padding to the HTML page

st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

st.title(UserDefinedString.page_education)

st.subheader("""
Master of Engineering (MEng), Software Engineering for Embedded Systems
""")

st.markdown("""
RPTU Kaiserslautern-Landau, 2017 – 2020

Organized in collaboration with the Fraunhofer Institute for Experimental Software Engineering (IESE), Kaiserslautern. 
This professional Master's program focused on software engineering with a special emphasis on embedded systems. 
The program provided theoretical knowledge and practical skills in project management, software quality assurance, 
software product line engineering, real-time systems, and more.

**Courses Covered:**
- Project Management
- Software Quality Assurance
- Software Product Line Engineering
- Requirements Engineering
- Software Architecture for Embedded Software Systems
- Component-Based Software Development
- Model-Based Component Engineering
- Real-Time Systems & Dependability Engineering

**Skills Acquired:**
- Pandas, Anaconda
- Software Requirements, Test Strategy
- Agile Methodologies, Scrum
- Embedded Systems, SDLC
- Requirements Analysis, SQL
- System Testing, J1939, CAN (Controller Area Network)
- Root Cause Analysis
""")

st.subheader("""
Bachelor of Technology (BTech), Electrical, Electronics, and Communications Engineering
""")

st.markdown("""
Integral University, Lucknow, Uttar Pradesh, 2008 – 2012
""")

st.subheader("""
Intermediate, Science
""")

st.markdown("""
Bright Land Inter College, Lucknow, 2006 – 2008
""")
