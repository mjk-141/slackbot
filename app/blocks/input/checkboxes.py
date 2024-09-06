import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from .label import label

@dataclass
class Checkboxes:
    ## 2개 입력 받기
    label_text: str
    action_id : str
    
    ## 입력 넣어도 좋고 안넣어도 좋고
    option: Optional[label] = None  # 딴 클래스 json 가져오기
    options_data: Optional[List[Dict[str, str]]] = None  # 옵션 데이터를 받을 필드를 추가합니다
    
    ## 여긴 입력 ㄴㄴ
    element: dict = field(init=False)
    type : str = field(init=False,default="input")
    
    def __post_init__(self):
        self.element = {
            "type": "checkboxes",
            "options": [],
			"action_id": self.action_id
        }
        
        # 옵션이 주어진 경우 options 필드에 적용합니다
        if self.options_data:
            for option in self.options_data:
                self.add_option(option['text'], option['value'])
        
        ## 이건 dont touch
        self.option = label(text=self.label_text)
            
        self.body = {
            "type": self.type,
            "element" : self.element,
            "label": self.option.to_dict()
        }
    
    def add_option(self, text: str, value: str):
        option = {
            "text": {
                "type": "plain_text",
                "text": text,
                "emoji": True
            },
            "value": value
        }
        self.element['options'].append(option)

    def json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, indent=4)