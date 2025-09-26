from rich.console import Console

console = Console()

def main():
    inventory = {
    "olma": 5,
    "banan": 3
}

    mahsulot = "anor"

    if mahsulot not in inventory:
        inventory[mahsulot] = 0

    console.print(inventory,style = 'underline green')

main()