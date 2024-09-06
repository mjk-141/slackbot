import json
from dataclasses import dataclass, field
from typing import Dict, Any, List
from .action import Action  # Ensure that this import statement works with your project structure
import time

@dataclass(unsafe_hash=True)
class Datepickers(Action):
    action_id_a : str
    action_id_b : str
    elements  : dict = field(init=False)
    placeholder : dict = field(init=False)
    initial_date : str = field(init=False, default_factory=lambda: time.strftime('%y/%m/%d'))
    body : List[str,Any] = field(init=False,default_factory=list)
    
    ## 초기화
    def __post_init__(self):
        self.placeholder = {
            "type" : "plain_text",
            "text" : "Select time", 
            "emoji":True
        }
        self.body = [
            {
                "type" : "datepicker",
                "initial_date" : self.initial_date,
                "placeholder" : self.placeholder,
                "action_id" : self.action_id_a
            },
            {         
                "type" : "datepicker",
                "initial_date" : self.initial_date,
                "placeholder" : self.placeholder,
                "action_id" : self.action_id_b
            }
        ]

    ## body를 json 형식으로 변환
    def json(self) -> str:
        return json.dumps(self.body,ensure_ascii=False, indent=4)