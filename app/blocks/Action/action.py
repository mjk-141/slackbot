from dataclasses import dataclass, field
from typing import Dict, Any
import json

@dataclass
class Action:
    type: str = field(init=False, default="actions")
    body: list[str, Any] = field(init=False, default_factory=list)

    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "type" : "action",
            "elements" : self.body
        }
        
    @property
    def pretty(self) -> None:
        print(json.dumps(self.body, ensure_ascii=False, indent=4))