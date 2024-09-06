import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from blocks.block import Block

@dataclass
class Button(Block):
    elements_data: Optional[List[Dict[str, str]]] = None  # 옵션 데이터를 받을 필드를 추가합니다
    type: str = field(init=False, default="button")
    text: Dict[str, str] = field(init=False)
    
    ## 여긴 입력 ㄴㄴ
    elements: List[Dict[str, Any]] = field(init=False, default_factory=list)
    type : str = field(init=False,default="actions")
    
    def __post_init__(self):
        # 옵션이 주어진 경우 options 필드에 적용합니다
        if self.elements_data:
            for element in self.elements_data:
                self.add_elements(element['text'],element['value'], element['action_id'])
                
        self.body = {
            "type": self.type,
            "elements": self.elements,
        }
    
    ## element 추가 부분(버튼을 가로로 늘릴지 결정)
    def add_elements(self, text: str, value: str, action_id : str):
        option = {
            "type" : "button",
            "text": {
                "type": "plain_text",
                "text": text,
                "emoji": True
            },
            "value": value,
            "action_id": action_id
        }
        self.elements.append(option)
        
    def json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, indent=4)