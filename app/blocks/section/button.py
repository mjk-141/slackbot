import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from .mrkdwn import MarkDown
from .section import Section


@dataclass
class Button(Section):
    ## 여기 까지 입력
    text: str
    markdown_text : str
    url: Optional[str] = None
    option: Optional[MarkDown] = None ##딴 클래스 json 가져오기
    
    ## 얘들은 입력 아님
    type: str = field(init=False, default="button")
    action_id: str = field(init=False, default="button-action")
    body: Dict[str, Any] = field(init=False)
    accessory : dict = field(init=False) ## 엑세사리

    def __post_init__(self):
        self.accessory = {
            "type": self.type,
            "text": {"type": "plain_text", "text": self.text, "emoji": True},
            "value": "TODO-FIX",
            "url": self.url,
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