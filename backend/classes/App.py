from dataclasses import dataclass
from typing import Dict, Callable
from websockets.legacy.server import WebSocketServerProtocol
from .ChatRoom import ChatRoom
from .User import User


@dataclass
class App:
    event_handlers: Dict[str, Callable]
    users: Dict[WebSocketServerProtocol, User]
    chat_rooms: Dict[str, ChatRoom]
    new_user_id: int = 0

    def __init__(self, event_handlers: Dict[str, Callable]) -> None:
        self.users = {}
        general_chat_room = ChatRoom("general", self.users)
        self.chat_rooms = {general_chat_room.name: general_chat_room}
        self.event_handlers = event_handlers

    async def handle_event(
        self, websocket: WebSocketServerProtocol, data: Dict
    ) -> None:
        if data["type"] not in self.event_handlers:
            return

        await self.event_handlers[data["type"]](self, websocket, data)
