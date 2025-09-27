from rich.console import Console

console = Console()

def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    active_users = []
    for username, info in users.items():
        if "active" in info:
            if info["active"] is True:
                active_users.append(username)
    return active_users

users = {
    "ali": {"active": True, "email": "ali@example.com"},
    "vali": {"active": False, "email": "vali@example.com"},
    "sami": {"active": True, "email": "sami@example.com"},
}

console.print(get_active_users(users),style = 'italic cyan')