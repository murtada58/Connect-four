import json

data = {}
with open("../eventTypes.json") as json_file:
    data = json.load(json_file)


class EventTypes:
    NEW_USER = data["NEW_USER"]
    USER_LEAVE = data["USER_LEAVE"]
    USER_DETAILS = data["USER_DETAILS"]
    USER_COUNT = data["USER_COUNT"]
    NAME_CHANGE = data["NAME_CHANGE"]
    MESSAGE = data["MESSAGE"]
