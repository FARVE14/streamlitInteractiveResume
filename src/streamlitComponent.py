"""
File Name: streamlitComponent

"""

__author__ = "Faisal Ahmed"

from pathlib import Path
import streamlit as st
from streamlit.components.v1 import html
from src.utilities import read_file_content
from src.dataModel import UserProfileDataModel
from dacite import from_dict
from src.html_component import (build_themed_image_link, html_card_template, format_for_html,
                                merge_css_js_for_card_template, html_badge)
import random

@st.cache_data
def load_css(css_file_path, load: bool = False) -> str | None:
    """
    Load css file.

    """
    css_content = read_file_content(css_file_path)
    if css_content and not load:
        return css_content
    if css_content and load:
        st.markdown(css_content, unsafe_allow_html=True)
    else:
        st.error("Unable to load the required css file")
    return None

@st.cache_data
def load_jss(jss_file_path) -> str | None:
    """
    Load external jss
    :param jss_file_path:
    :return:
    """
    jss_content = read_file_content(jss_file_path)
    if jss_content:
       return jss_content
    else:
        st.error("Unable to load the required jss")
        return None

@st.cache_data
def read_profile_data(profile_data_path:str | Path) -> UserProfileDataModel | None:
    """
    Read profile data
    """
    profile_data = read_file_content(profile_data_path)
    try:
        return from_dict(data_class=UserProfileDataModel, data=profile_data)
    except Exception as e:
        st.error(f"❌ Failed to read profile data: {e}")
        return None


@st.cache_data
def publish_sidebar_details(
        user_data: UserProfileDataModel,
        profile_image_path: Path,
        logo_folder_path: Path
) -> None:
    """
    Publish sidebar details
    """
    st.image(image=profile_image_path / "profile.png", width='stretch')
    st.divider()
    user_profile_contact_data = user_data.profile.contact
    for index, keys in enumerate(user_data.profile.contact.keys()):
        ref_method_name = keys
        ref_link = user_profile_contact_data[keys]
        ref_image = (logo_folder_path / f"{ref_method_name}.png").__str__()
        st.markdown(
            build_themed_image_link(
                ref_link=ref_link,
                image_path=ref_image,
                alt_text=ref_method_name),
            unsafe_allow_html=True,
        )


@st.cache_data
def publish_dashboard_details(
        user_data: UserProfileDataModel
) -> None:
    """
    Publish dashboard details
    """
    year_of_experience = user_data.profile.experience
    no_organization = len(user_data.organization)
    no_of_roles = sum([len(organization.role) for organization in user_data.organization])
    projects = (sum([len(organization.projects) for organization in user_data.organization])
                + len(user_data.personalProjects.projects))
    list_col_objs = st.columns(3)

    with list_col_objs[0]:
        st.metric(f"⏳ Years of Experience", year_of_experience)
    with list_col_objs[1]:
        st.metric(f"🧑‍💼 Roles held across {no_organization} Org", no_of_roles)

    with list_col_objs[2]:
        st.metric(f"✅ Projects Completed", projects)


    st.subheader("Career Focus, Highlights & Impact")
    list_col_objs = st.columns(2)
    with list_col_objs[0]:
        container = st.container(border=True)
        for data in user_data.profile.key_skills:
            for skill, description in data.items():
                container.markdown(f"<h5>✨ {skill}</h5>", unsafe_allow_html=True)
                container.write(description)
    with list_col_objs[1]:
        container = st.container(border=True)
        container.markdown("<h5>🏆 Achievements</h5>", unsafe_allow_html=True)
        for data in user_data.profile.achievements:
            container.write(f"🌟 {data}")

    st.subheader("🏢 Company Overview")
    container = st.container(border=True)
    for company in user_data.organization:
        with container:
            list_col_objs = st.columns(4)
            with list_col_objs[0]:
                st.write(f"👥 {company.name}")
            with list_col_objs[len(list_col_objs) - 2]:
                st.write(f"{company.from_date} - {company.end_date}")
            with list_col_objs[len(list_col_objs) - 1]:
                st.write(f"{company.location}")


def publish_career_timeline(user_data: UserProfileDataModel) -> None:
    """
    Publish career timeline
    """
    st.header("Explore my journey")
    for organization in user_data.organization:
        container = st.container(border=True)
        with container:
            st.markdown(f"### {organization.name}  | {organization.from_date} - {organization.end_date} | "
                        f"{organization.location}")
            for role in organization.role:
                st.markdown(f"#### {role.title} | {role.from_date} - {role.end_date}")
                [st.markdown(f"- {responsibilities}") for responsibilities in role.responsibilities]


def publish_project_showcase(user_data: UserProfileDataModel,
                             js_template: str,
                             css_template: str) -> None:
    """
    Publish project showcase

    """
    total_projects = (sum([len(organization.projects) for organization in user_data.organization]) +
                      len(user_data.personalProjects.projects))
    st.header(f"Explore my Projects: {total_projects} Projects")
    # --- Configuration ---
    card_pixel_width  = 360  # Increased from 250 to fit ~3 cards wide
    margin_right = 15
    total_card_width = card_pixel_width + margin_right

    colors = ["#4a5d73", "#8c94a0", "#7fa58a", "#5b6e7f", "#8d6a8a", "#a1a57f"]
    for organization in user_data.organization +  [user_data.personalProjects]:
        no_projects = len(organization.projects)
        if no_projects == 0:
            continue
        cards_data = []
        st.header(f"{organization.name} : {no_projects} Projects")
        for index, project in enumerate(organization.projects):
            cards_data.append({
                "id": f"P-{index:02d}",
                "title": project.title,
                "content": project.description,
                "details": project.details,
                "color": colors[index % len(colors)],
                "skills": project.skills_used
            })

        # 1. Generate all the card HTML content
        all_cards_html = "".join([
            html_card_template(
                title=data["title"],
                content=data["content"],
                color=data["color"],
                details_html=data["details"],
                tags=data["skills"],
            ).format(
                 details_html=format_for_html(data["details"])
            )
            for data in cards_data
        ])

        js_content = js_template.replace("TOTAL_CARD_WIDTH_PLACEHOLDER", str(total_card_width))

        project_data = merge_css_js_for_card_template(
            js_content=js_content,
            css_content=css_template,
            all_cards_html=all_cards_html
        )
        html(project_data, height=500)


def publish_skills(user_data: UserProfileDataModel, css_file_path: str | None = None) -> None:
    """
    Publish skill showcase

    """
    st.header("Skills")
    if css_file_path:
        st.markdown(f"""<style>{load_css(css_file_path=css_file_path)}</style>""",
                    unsafe_allow_html=True)

    badge_colors = [
        "#AEC6CF",  # Soft Cadet Blue
        "#ADD8E6",  # Light Sky Blue
        "#C1E1C1"  # Soft Pastel Green
    ]

    all_skills: set = set()

    for group in user_data.skills:
        all_skills.update(group.technologies)

    selected_skills : list[str] = st.multiselect(
        "Filter by specific skills",
        options=sorted(list(all_skills)),
        default=[]
    )

    for skill_group in user_data.skills:
        container = st.container(border=True)
        with container:
            st.subheader(skill_group.category)
            # 2. Build a single HTML string containing all badges
            badge_html = ""
            for skill in skill_group.technologies:
                if skill in selected_skills or not selected_skills:
                      badge_html += html_badge(
                          skill=skill,
                          color=random.choice(badge_colors)
                      )

            # 3. Render the full HTML string
            st.markdown(badge_html, unsafe_allow_html=True)



def publish_education(user_data: UserProfileDataModel) -> None:
    """
    Publish education showcase
    """

    st.header("Education")

    for edu in user_data.education:
        # Use a container for a clean, professional box around each education entry
        with st.container(border=True):

            # 1. Degree Title and Institution
            st.subheader(f"🎓 **{edu.degree_name}** | *{edu.course_name}*")
            st.markdown(f"**{edu.institute_name}**", unsafe_allow_html=True)
            st.caption(f"{edu.from_date} - {edu.end_date}")

            # 2. Overview (if available)
            if edu.overview:
                # Use st.write for the body text
                st.markdown(edu.overview)


def publish_references(user_data: UserProfileDataModel):
    """
    Publish references showcase
    """
    st.header("References")
    for ref in user_data.references:
        # Use a container for a clean, professional box around each reference entry
        with st.container(border=True):

            st.subheader(f"👤 {ref.name}")

            # 2. Organization (Secondary text)
            if ref.organization:
                st.markdown(f"*{ref.organization}*", unsafe_allow_html=True)

            # 3. Contact (Tertiary text, often linked for quick access)
            if ref.contact:
                # Create a mailto link for easy emailing
                contact_link = f"mailto:{ref.contact}"
                st.caption(f"Contact: [{ref.contact}]({contact_link})")