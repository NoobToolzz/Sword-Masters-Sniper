import random
import string
import requests

from rich import print
from pathlib import Path


class AccountManager:
    def __init__(self, accounts_file="accounts.txt"):
        self.root_dir = Path(__file__).resolve().parent.parent
        self.accounts_file = self.root_dir / "data" / accounts_file

    def get_tokens(self):
        tokens = []
        with open(self.accounts_file) as f:
            accounts = f.readlines()

        for account in accounts:
            account = account.strip()
            if ":" in account:
                username, password = account.split(":")
                token = self.login(username, password)
                if token:
                    tokens.append(token)
            else:
                tokens.append(account)

        return tokens

    def login(self, username, password):
        r = requests.post(
            "https://loadbalancer.swordmasters.io/api/user/login",
            json={"username": username, "password": password},
        )
        if r.status_code == 200:
            return r.json().get("token")
        return None

    def register(self, num_accounts=None):
        if num_accounts is None:
            num_accounts = 1

        def generate_password():
            return "".join(
                random.choices(
                    string.ascii_letters + string.digits, k=random.randint(4, 6)
                )
            )

        tokens = []
        for account_number in range(1, int(num_accounts) + 1):
            token_request = requests.post(
                "https://loadbalancer.swordmasters.io/api/server/findServer",
                json={"token": None},
            )

            if token_request.status_code == 200:
                tr_data = token_request.json()
                token, foundServer, altServer = (
                    tr_data["token"],
                    tr_data["data"]["foundServer"],
                    tr_data["data"]["alternativeServer"],
                )

                print(
                    f"[bold blue]Account {account_number} - Found Server: [cyan]{foundServer}"
                )
                print(
                    f"[bold magenta]Account {account_number} - Alternative Server: [cyan]{altServer}"
                )

            password = generate_password()

            r = requests.post(
                "https://loadbalancer.swordmasters.io/api/user/register",
                json={"token": token, "password": password},
            )
            if r.status_code == 200:
                new_token = r.json().get("token")
                with open(self.accounts_file, "a") as f:
                    f.write(new_token + "\n")
                tokens.append(new_token)  # The token stays the same but whatever

        return tokens if tokens else None
