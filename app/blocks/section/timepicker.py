import json
import time
from dataclasses import dataclass, field
from .mrkdwn import MarkDown
from typing import Optional, Dict, Any

@dataclass
class Timepicker:
    action_id: str
    markdown_text : str
    
    type: str = field(init=False, default="timepicker")
    initial_date: str = field(init=False, default_factory=lambda: time.strftime('%H:%M'))
    placeholder: dict = field(init=False)

    def __post_init__(self):
        self.placeholder = {
            "type": "plain_text",
            "text": "Select Time",
            "emoji": True
        }
        
        self.accessory = {
            "type": self.type,
            "initial_time": self.initial_date,
            "placeholder": self.placeholder,
            "action_id": self.action_id
        }
        
        self.option = MarkDown(msg=self.markdown_text)
        
        self.body = {
            "type": self.option.to_dict()['type'],
            "text": self.option.to_dict()['text'],
            "accessory" : self.accessory
        }
        
    def json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, indent=4)
