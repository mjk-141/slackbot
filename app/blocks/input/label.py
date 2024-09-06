import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any

@dataclass
class label:
    text: str
    def __post_init__(self):
        self.body = {
            "type": "plain_text",
            "text": self.text,
            "emoji": True
        }
    
    ## 외부 호출용
    def json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, indent=4)
    
    ## 딴 클래스에서 호출용
    def to_dict(self) -> dict:
        return self.body