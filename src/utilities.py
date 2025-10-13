"""
File Name: 

"""

__author__ = "Faisal Ahmed"

import base64
from pathlib import Path
import json
from dacite.data import Data


def img_to_bytes(image_path: str):
    """
    Convert image to bytes.
    :param image_path:
    :return: bytes
    """
    return base64.b64encode(
        Path(image_path).read_bytes()
    ).decode("utf-8")


def read_file_content(file_path: str) -> str | list[str] | dict | Data | None:
    """
    Load file content.
    :param file_path:
    :return:
    """
    file_path = str(file_path)
    try:
        with open(file_path, 'r') as f:
            if file_path.endswith('.json'):
                return json.load(f)
            return f.read()
    except FileNotFoundError as e:
        print(e)
        return None
    except Exception as e:
        print(e)
        return None
