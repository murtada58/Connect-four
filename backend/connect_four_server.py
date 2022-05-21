#!/usr/bin/env python3

import asyncio
import json
import websockets
from datetime import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env.dev')
load_dotenv(dotenv_path)

PEPPER = os.environ.get("PEPPER")
SERVER_IP = os.environ.get("SERVER_IP")
SERVER_PORT = os.environ.get("SERVER_PORT")

USERS = set()
USERS_DETAILS = {}
CHAT_ROOMS = {"general": USERS}
new_user_id = 1


async def game(websocket, path):
    global new_user_id
    try:
        new_user_id += 1
        USERS.add(websocket)
        USERS_DETAILS[websocket] = {
            "userId": new_user_id,
            "username": "Guest",
            "usernameColor": "#FF0000"
        }
        await websocket.send(json.dumps({
            "type": "username",
            "userId": USERS_DETAILS[websocket]["userId"],
            "username": USERS_DETAILS[websocket]["username"],
            "usernameColor": USERS_DETAILS[websocket]["usernameColor"]
        }))
        websockets.broadcast(USERS, json.dumps({
            "type": "user",
            "count": len(USERS)
        }))
        print("New user joined: ")

        async for message in websocket:
            data = json.loads(message)
            print("Recieved message: " + message)

            if data["action"] == "nameChange":
                if len(data["username"]) > 20:
                    return
                USERS_DETAILS[websocket]["username"] = data["username"]

            elif data["action"] == "message":
                if websocket not in CHAT_ROOMS[data["chatRoom"]]:
                    return
                if len(data["message"].strip()) == 0:
                    return
                websockets.broadcast(CHAT_ROOMS[data["chatRoom"]], json.dumps({
                    "type": "message",
                    "chatRoom": data["chatRoom"],
                    "userId": USERS_DETAILS[websocket]["userId"],
                    "username": USERS_DETAILS[websocket]["username"],
                    "usernameColor": USERS_DETAILS[websocket]["usernameColor"],
                    "message": data["message"],
                    "time": datetime.now().strftime('%I:%M:%p')
                }))

    finally:
        USERS.remove(websocket)
        websockets.broadcast(USERS, json.dumps({
            "type": "user",
            "count": len(USERS)
        }))


async def main():
    async with websockets.serve(game, SERVER_IP, SERVER_PORT):  # , ssl=ssl_context):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
