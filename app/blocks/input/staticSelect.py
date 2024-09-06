import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from .label import label
from app.Credentials.AWS.aws_credentials import *
from app.Credentials.Gitlab.gitlab_credentials import *

COMPANY_ID = ["DGMONG","HAMALAB","CUBALTO","UMAY","WIKIFOKI", 
             "SINSA", "CMB", "SAFESCHOOL", "MANAGEON", "ION","PPNTALK"]

GITLAB_COMPANY_ID = ["203","199","88","58","46","45", "43", "2"]

@dataclass
class Static_Select:
    label_text: str
    text : str
    action_id : str
    type : str = field(init=False,default="input")
    placeholder : dict = field(init=False)
    element: dict = field(init=False)
    options_data: Optional[List[Dict[str, str]]] = None
    option: Optional[label] = None ##딴 클래스 json 가져오기
    
    def __post_init__(self):
        self.placeholder = {
            "type" : "plain_text",
            "text" : self.text, 
            "emoji":True
        }
        
        # 옵션 데이터를 가져옴 fetch_aws_repositories()
        if self.options_data in COMPANY_ID:
            self.options_data = fetch_aws_repositories(self.options_data)
        elif self.options_data in GITLAB_COMPANY_ID:
            self.options_data = fetch_gitlab_repositories_options(self.options_data)
        
        self.element = {
            "type": "static_select",
            "placeholder": self.placeholder,
			"options": []
        }
        
        # 옵션 추가
        for option in self.options_data:
            self.add_option(option['text'], option['value'])
            
        self.option = label(text=self.label_text)
            
        self.body = {
            "dispatch_action": False,
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
        self.element["options"].append(option)
        
    def json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, indent=4)