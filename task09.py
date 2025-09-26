from rich.console import Console

console = Console()

def main():
    users = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
]

    for user in users:
      user['active'] = False

    console.print(users,style = 'blue')

main()