import json
from dataclasses import dataclass, field
from typing import Dict, Any, List

@dataclass
class Block:
    type: str = field(init=False, default="blocks")
    body: Dict[str, Any] = field(init=False)
    blocks: List[Dict[str, Any]] = field(default_factory=list)
    
    def __post_init__(self):
        self.body = {
            "blocks": self.blocks
        }

    @property
    def to_dict(self) -> Dict[str, Any]:
        return self.body

    @property
    def pretty(self) -> None:
        print(json.dumps(self.body, ensure_ascii=False, indent=4))
        
    def json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, indent=4)

    def add_block(self, block: Dict[str, Any]):
        self.blocks.extend(block)
