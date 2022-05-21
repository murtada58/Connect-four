#!/usr/bin/env python3

import asyncio
import json
import websockets
from datetime import datetime


# set to "localhost" or your servers ip if you want to host your own server
SERVER_IP = "localhost"  # "176.58.109.37"
PORT = 6789

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
                USERS_DETAILS[websocket]["username"] = data["username"]

            elif data["action"] == "message":
                if (websocket not in CHAT_ROOMS[data["chatRoom"]]):
                    return
                if (len(data["message"].strip()) == 0):
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
    async with websockets.serve(game, SERVER_IP, PORT):  # , ssl=ssl_context):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
