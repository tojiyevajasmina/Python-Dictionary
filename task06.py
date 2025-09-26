from rich.console import Console

console = Console()

def main():
    car = {
    "brand": "Kawasaki",
    "model": "kawasaki Ninja H2R",
    "color": "black"
}

    key = input("Qaysi kalitni ko'rmoqchisiz? ")
    value = car.get(key, "Topilmadi")

    console.print(value,style = "bold cyan")

main()
