"""
File Name: 

"""

__author__ = "Faisal Ahmed"

from src.utilities import img_to_bytes


def build_themed_image_link(ref_link: str, image_path: str, alt_text: str = "",
                            style: str ='width:20%; height:20%') -> str:
    """
    Returns HTML for a theme-aware linked image that adapts to Streamlit's dark/light theme.
    """
    return f"""
        <div style="
            background-color: var(--background-color);
            color: var(--text-color);
            padding: 0.5rem;
            border-radius: 10px;
            display: inline-block;
            width: 100%;
        ">
            <a href="{ref_link}" target="_blank" style="text-decoration:none; display:block;">
                <img src="data:image/png;base64,{img_to_bytes(image_path)}"
                     alt="{alt_text}" style="{style}">
            </a>
        </div>
        """

def html_card_template(title: str, color: str, content: str, details_html:str, tags: list[str] | None = None) -> str:
    """
    Returns HTML for card-template
    """
    tags = tags or []
    tags_html = "".join(f'<span class="tag">{tag}</span>' for tag in tags)

    return f"""
    <div class="card" 
         style="background-color: {color};">
        <div class="card-header">{title}</div>
        <div class="card-content">
            <div class="card-body">{content}</div>
            <div class="card-details-area">
                <p><strong>Details:</strong></p>
                <p>{details_html}</p>
            </div>
            <div class="card-tags">
                {tags_html}
            </div>
        </div>
    </div>"""

# Helper function to convert newlines to <br> for HTML display
def format_for_html(text):
    if text is None:
        return text
    return text.replace("\n", "<br>")


def merge_css_js_for_card_template(
        css_content: str, js_content: str, all_cards_html: str
) -> str :
    """

    """
    return f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        {css_content}
    </style>
</head>
<body>

<div class="slider-container">
    <button id="prevBtn" class="arrow-btn" onclick="slide(-1)">&#9664;</button>
    <div class="card-track-wrapper">
        <div id="cardTrack" class="card-track">
            {all_cards_html}
        </div>
    </div>
    <button id="nextBtn" class="arrow-btn" onclick="slide(1)">&#9654;</button>
</div>

<script>
    {js_content}
</script>

</body>
</html>
"""


def html_badge(skill: str, color: str, text_color: str = "#36454F") -> str:
    """
    Returns HTML for badge
    """
    badge_style = f"""background-color: {color};
                    color: {text_color};
                    padding: 4px 8px; /* Small padding for less gap */
                    margin: 0px 5px 5px 0px; /* Crucial: 0px left/right margin for tight stack, 5px bottom margin for wrapping */
                    border-radius: 5px;
                    display: inline-block; /* Allows them to flow horizontally and wrap */
                    font-size: 0.9em;
                    font-weight: 500;
"""
    return f'<span style="{badge_style}">{skill}</span>'