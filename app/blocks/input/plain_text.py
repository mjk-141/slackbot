import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from .label import label

@dataclass
class Plain_text:
    label_text: str
    action_id : str
    text : str
    type : str = field(init=False,default="input")
    element: dict = field(init=False)
    option: Optional[label] = None ##딴 클래스 json 가져오기
    
    def __post_init__(self):
        self.element = {
            "type": "plain_text_input",
			"action_id": self.action_id,
            "placeholder": {
				"type": "plain_text",
				"text": self.text
			}
        }
        
        self.option = label(text=self.label_text)
            
        self.body = {
            "dispatch_action": False,
            "type": self.type,
            "element" : self.element,
            "label": self.option.to_dict()
        }
    
    def json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, indent=4)