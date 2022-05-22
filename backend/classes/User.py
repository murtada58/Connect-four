from dataclasses import dataclass
from typing import Dict
from websockets.legacy.server import WebSocketServerProtocol


@dataclass
class User:
    websocket: WebSocketServerProtocol
    id: int
    name: str
    color: str

    def to_dict(self) -> Dict[str, str]:
        return {"id": self.id, "name": self.name, "color": self.color}
