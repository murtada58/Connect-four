from dataclasses import dataclass
from datetime import datetime
from typing import Dict
from .User import User


@dataclass
class Message:
    number: int
    user: User
    text: str
    time: str = datetime.now().strftime("%I:%M:%p")

    def to_dict(self) -> Dict:
        return {
            "number": self.number,
            "user": self.user.to_dict(),
            "text": self.text,
            "time": self.time,
        }
