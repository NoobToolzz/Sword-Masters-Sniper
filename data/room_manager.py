import os

from rich import print


class RoomManager:
    def print_room_status(self, response, room_uid, relative_time):
        if response["room"]["clients"] == 1:  # You're the only one then
            return

        print(
            f"""
[bold cyan]Room Status:[/]
• Clients: [green]{response['room']['clients']}[/green]/[yellow]{response['room']['maxClients']}[/yellow]
• Process ID: [magenta]{response['room']['processId']}[/magenta]
• Room ID: [blue]{room_uid}[/blue] ([dim]{response['room']['roomId']}[/dim])
• Session ID: [red]{response['sessionId']}[/red]
• Room creation time: [yellow]{relative_time}[/yellow] ([dim]{response['room']['createdAt']}[/dim])

• Join Link: [cyan]https://swordmasters.io/#{room_uid}[/cyan]
"""
        )

    def save_room_info(self, response, room_uid, relative_time, now):
        if response["room"]["clients"] == 1:
            return

        folder_name = f"Sniped/[{now.strftime('%d-%m-%y')}"
        os.makedirs(folder_name, exist_ok=True)

        with open(os.path.join(folder_name, "snipes.txt"), "a") as file:
            file.write(
                f"""===============================
Clients: {response['room']['clients']}/{response['room']['maxClients']}
Room ID: {room_uid} ({response['room']['roomId']})
Creation Time: {relative_time} ({response['room']['createdAt']})

Join link: https://swordmasters.io/#{response['room']['roomId']}
===============================
"""
            )
