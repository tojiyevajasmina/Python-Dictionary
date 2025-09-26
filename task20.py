from rich.console import Console

console = Console()

def main():
    permissions = {"read": True, "write": False, "delete": True}

    for key in permissions:
        if permissions[key] == True:
         console.print(key, style = 'italic cyan')
     
main()