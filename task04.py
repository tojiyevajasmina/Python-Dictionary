from rich.console import Console

console = Console()

def main():
    car = {"brand": "Chevrolet",
           "model": "Cobalt", 
           "color": "white"
}


    console.print(f"Brand: {car['brand']}", style="cyan")
    console.print(f"Color: {car['color']}", style="green") 

main()
