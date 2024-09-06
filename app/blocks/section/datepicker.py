import sys
import os

# 부모 디렉토리를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(parent_dir)

import json
import time
from dataclasses import dataclass, field, asdict
from .mrkdwn import MarkDown
from blocks.block import Block

@dataclass
class Datepicker:
    action_id: str
    markdown_text : str
    
    type: str = field(init=False, default="datepicker")
    initial_date: str = field(init=False, default_factory=lambda: time.strftime('%Y-%m-%d'))
    placeholder: dict = field(init=False)
    accessory : dict = field(init=False) ## 엑세사리
    
    ## __post_init__ 메서드에서 초기화를 실시(무조건 존재!)
    def __post_init__(self):
        self.placeholder = {
            "type": "plain_text",
            "text": "Select a date",
            "emoji": True
        }
        
        self.accessory = {
            "type": self.type,
            "initial_date": self.initial_date,
            "placeholder": self.placeholder,
            "action_id": self.action_id
        }
        
        self.option = MarkDown(msg=self.markdown_text)
        
        self.body = {
            "type": self.option.to_dict()['type'],
            "text": self.option.to_dict()['text'],
            "accessory" : self.accessory
        }
    
    ## body를 json 형식으로 변환
    def json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, indent=4)