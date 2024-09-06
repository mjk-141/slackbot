import json
from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Section:
    type: str = field(init=False, default="section")
    body: Dict[str, Any] = field(init=False, default_factory=dict)

    @property
    def to_dict(self) -> Dict[str, Any]:
        return self.body

    @property
    def pretty(self) -> None:
        print(json.dumps(self.body, ensure_ascii=False, indent=4))