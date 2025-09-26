from rich.console import Console

console = Console()

def main():
    data = {
    "name": "JASMINA",
    "age": 18,
    "city": "SAMARQAND"
    }

    key = input("Kalit nomini kiriting: ")

    if key in data:
        data.pop(key)
        console.print(f"'{key}' kaliti o'chirildi.",style = 'italic green')
    else:
        console.print("Bunday kalit yo'q.",style = 'italic red')

    console.print("Yangi dict:", data, style = 'italic yellow')

main()