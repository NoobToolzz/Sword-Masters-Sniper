import time
import json
import pytz
import requests
import random

from rich import print
from pathlib import Path
from datetime import datetime
from data.room_manager import RoomManager
from data.account_manager import AccountManager
from dateutil.relativedelta import relativedelta


class Sniper:
    def __init__(self, config_path="config.json"):
        self.root_dir = Path(__file__).resolve().parent.parent
        self.config = self.load_config(self.root_dir / config_path)
        self.target_clients = self.config["clients"]
        self.attempts = 0
        self.room_manager = RoomManager()
        self.account_manager = AccountManager()

    def load_config(self, path):
        with open(path) as f:
            return json.load(f)

    def get_tokens(self):
        return self.account_manager.get_tokens()

    def snipe(self):
        try:
            while True:
                self.attempts += 1
                print(
                    f"[white][[bold green]SNIPER[white]] [yellow]Sniping[/yellow] ([cyan]{self.attempts}[/cyan])",
                    end="\r",
                )

                response = self.join_or_create_room()
                room_uid = self.get_room_uid(response["room"]["roomId"])

                if response["room"]["clients"] <= self.target_clients:
                    self.process_room(response, room_uid)

                # time.sleep(5)
        except KeyboardInterrupt:
            pass

    def join_or_create_room(self):
        tokens = self.get_tokens()
        if not tokens:
            print("[bold red]No tokens available![/bold red]")
            return None

        random_token = random.choice(tokens)
        r = requests.post(
            "https://eu1.swordmasters.io/matchmake/joinOrCreate/world_trade",
            json={"accessToken": random_token},
        )
        return r.json()

    def get_room_uid(self, room_id):
        r_uid = requests.post(
            "https://loadbalancer.swordmasters.io/api/server/getRoomUID",
            json={"roomId": room_id},
        )
        return r_uid.json()["roomUID"]

    def process_room(self, response, room_uid):
        created_at = datetime.fromisoformat(
            response["room"]["createdAt"].replace("Z", "+00:00")
        )
        now = datetime.now(pytz.UTC)
        delta = relativedelta(now, created_at)

        relative_time = (
            f"{delta.hours}h {delta.minutes}m {delta.seconds}s ago"
            if delta.days == 0
            else f"{delta.days}d {delta.hours}h ago"
        )

        self.room_manager.print_room_status(response, room_uid, relative_time)
        self.room_manager.save_room_info(response, room_uid, relative_time, now)
