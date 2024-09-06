import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from .section import Section


@dataclass
class MarkDown:
    msg: str
    # option: Optional[Section] = None
    type: str = field(init=False, default="mrkdwn")
    text : dict = field(init=False) ## 엑세사리

    def __post_init__(self):
        self.text = {
            "type": self.type,
            "text": self.msg
        }
        self.body = {
            "type": "section",
            "text": self.text
        }

    def json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, indent=4)
    
    ## 딴 클래스에서 호출용
    def to_dict(self) -> dict:
        return self.body