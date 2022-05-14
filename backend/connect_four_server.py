#!/usr/bin/env python3

import asyncio
import json
import websockets
from datetime import datetime


# set to "localhost" or your servers ip if you want to host your own server
SERVER_IP = "localhost"  # "176.58.109.37"
PORT = 6789

USERS = set()

new_user_id = 1


async def game(websocket, path):
    global new_game_id
    global new_user_id
    try:
        USERS.add(websocket)
        new_user_id += 1
        websockets.broadcast(USERS, json.dumps({"message": "New user joined"}))
        print("New user joined")

        async for message in websocket:
            data = json.loads(message)
            print("Recieved message: " + message)
            if data["action"] == "name_change":
                pass
            else:
                pass
    finally:
        USERS.remove(websocket)


async def main():
    async with websockets.serve(game, SERVER_IP, PORT):  # , ssl=ssl_context):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
