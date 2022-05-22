from typing import Dict
from websockets.legacy.server import WebSocketServerProtocol
import sys

sys.path.append("../classes")
from classes.App import App


async def name_change_event(
    app: App, websocket: WebSocketServerProtocol, data: Dict
) -> None:
    if len(data["user"]["name"]) > 20:
        return

    app.users[websocket].name = data["user"]["name"]
