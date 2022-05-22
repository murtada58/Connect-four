import json
from typing import Dict
import websockets
from websockets.legacy.server import WebSocketServerProtocol
import sys

sys.path.append("../classes")
from classes.EventTypes import EventTypes
from classes.App import App


async def user_leave_event(
    app: App, websocket: WebSocketServerProtocol, data: Dict
) -> None:
    del app.users[websocket]
    websockets.broadcast(
        app.users,
        json.dumps({"type": EventTypes.USER_COUNT, "count": len(app.users)}),
    )

    print("User left")
