import os

from rich import print
from rich.prompt import Prompt
from data.sniper import Sniper
from data.others import Others
from rich.console import Console
from data.account_manager import AccountManager


def main():
    console = Console()
    Others.clean_up_cache()  # Me no like __pycache__ garbage

    while True:
        print("[white][[bold cyan]1[white]] [cyan]Register Accounts")
        print("[white][[bold green]2[white]] [green]Start Sniping")
        print("[white][[bold red]3[white]] [red]Exit")

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3"], default="3")

        if choice == "1":
            num_accounts = Prompt.ask("Amount of accounts you want to register")
            os.system("cls||clear")

            account_manager = AccountManager()
            print("[bold green]Registering Accounts...")
            new_token = account_manager.register(num_accounts=num_accounts)
            if new_token:
                print(f"[bold green]Registered the following token(s): {new_token}")
            else:
                print("[bold red]Failed to register account(s).")

        elif choice == "2":
            os.system("cls||clear")

            sniper = Sniper()
            sniper.snipe()

        elif choice == "3":
            print("[bold yellow]Exiting...")
            break


if __name__ == "__main__":
    main()
