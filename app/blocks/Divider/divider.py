import json
from dataclasses import *
from typing import Optional, Dict, Any


@dataclass
class Divder:
    type : str = field(init=False,default="divider")
    body: Dict[str, Any] = field(init=False)
    
    def __post_init__(self):
        self.body = dict(
            type=self.type
        )

    def json(self):
        return json.dumps(self.body,ensure_ascii=False, indent=4)
