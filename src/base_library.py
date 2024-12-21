import base64
from pathlib import Path


def img_to_bytes(img_path: str):
    """

    """
    img_bytes = Path(img_path).read_bytes()
    return base64.b64encode(img_bytes).decode()


def img_to_html(img_path: str, style='width:10%; height:10%') -> str:
    """

    """
    return f"<img src='data:image/png;base64,{img_to_bytes(img_path)}' style='{style}' class='img-fluid'>"
