from pathlib import Path
from typing import List, Literal, Optional, Union

from nonebot import get_driver
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    gpt_2_api: str = "http://127.0.0.1:5000"

gpt2_config = Config.parse_obj(get_driver().config)