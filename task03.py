from rich.console import Console

console = Console()

def main():
    user1 = {'name': 'Ahmad', 'email': 'ahmad@.com'}
    user2 = {'name': 'Laylo', 'email': 'laylo@.com'}

    users = [user1, user2]

    console.print(users, style='magenta')

main()
