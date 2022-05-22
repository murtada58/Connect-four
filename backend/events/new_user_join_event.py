import json
from typing import Dict
import websockets
from websockets.legacy.server import WebSocketServerProtocol
import sys

sys.path.append("../classes")
from classes.User import User
from classes.EventTypes import EventTypes
from classes.App import App

sys.path.append("../helpers")
from helpers.get_random_colour import get_random_colour


async def new_user_join_event(
    app: App, websocket: WebSocketServerProtocol, data: Dict
) -> None:
    app.new_user_id += 1

    app.users[websocket] = User(
        websocket,
        app.new_user_id,
        "Guest",
        get_random_colour(min_lightness=50, min_saturation=80),
    )

    await websocket.send(
        json.dumps(
            {
                "type": EventTypes.USER_DETAILS,
                "user": app.users[websocket].to_dict(),
            }
        )
    )
    websockets.broadcast(
        app.users,
        json.dumps({"type": EventTypes.USER_COUNT, "count": len(app.users)}),
    )

    print("New user joined")
