from dataclasses import dataclass
import json
from typing import Dict, List
import websockets
from websockets.legacy.server import WebSocketServerProtocol
from .User import User
from .Message import Message
from .EventTypes import EventTypes


@dataclass
class ChatRoom:
    name: str
    users: Dict[WebSocketServerProtocol, User]
    messages: List[Message]

    def __init__(self, name, users) -> None:
        self.name = name
        self.users = users
        self.messages = []

    def message_event(self, websocket: WebSocketServerProtocol, data: Dict) -> None:
        if websocket not in self.users or len(data["text"].strip()) == 0:
            return

        message = Message(len(self.messages), self.users[websocket], data["text"])

        self.messages.append(message)

        websockets.broadcast(
            self.users,
            json.dumps(
                {
                    "type": EventTypes.MESSAGE,
                    "chatRoom": self.name,
                    "message": message.to_dict(),
                }
            ),
        )
