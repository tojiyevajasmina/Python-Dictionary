from rich.console import Console

console = Console()

def main():
    car = {"brand": "BMW", "model": "M5 F90 ", "color": "black"}

    year = car.get("year", 2020)

    console.print("Year:", year , style = 'italic black')

main()
