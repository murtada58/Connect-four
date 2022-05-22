#!/usr/bin/env python3

import asyncio
import json
import websockets
from websockets.legacy.server import WebSocketServerProtocol
import os
from os.path import join, dirname
from dotenv import load_dotenv
from classes.App import App
from classes.EventTypes import EventTypes
from events.new_user_join_event import new_user_join_event
from events.user_leave_event import user_leave_event
from events.name_change_event import name_change_event
from events.message_event import message_event


dotenv_path = join(dirname(__file__), ".env.dev")
load_dotenv(dotenv_path)

PEPPER = os.environ.get("PEPPER")
SERVER_IP = os.environ.get("SERVER_IP")
SERVER_PORT = os.environ.get("SERVER_PORT")

app = App(
    {
        EventTypes.NEW_USER: new_user_join_event,
        EventTypes.USER_LEAVE: user_leave_event,
        EventTypes.NAME_CHANGE: name_change_event,
        EventTypes.MESSAGE: message_event,
    }
)


async def game(websocket: WebSocketServerProtocol, path: str) -> None:
    try:
        await app.handle_event(websocket, {"type": EventTypes.NEW_USER})

        async for message in websocket:
            data = json.loads(message)
            print(
                "\nReceived message: \n",
                json.dumps(data, indent=4, sort_keys=True),
                end="\n\n",
            )

            await app.handle_event(websocket, data)

    finally:
        await app.handle_event(websocket, {"type": EventTypes.USER_LEAVE})


async def main() -> None:
    async with websockets.serve(game, SERVER_IP, SERVER_PORT):  # , ssl=ssl_context):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
