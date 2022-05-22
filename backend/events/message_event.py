from typing import Dict
from websockets.legacy.server import WebSocketServerProtocol
import sys

sys.path.append("../classes")
from classes.App import App


async def message_event(
    app: App, websocket: WebSocketServerProtocol, data: Dict
) -> None:
    if data["chatRoom"] not in app.chat_rooms:
        return

    app.chat_rooms[data["chatRoom"]].message_event(websocket, data["message"])
