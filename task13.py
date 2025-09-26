from rich.console import Console

console = Console()

def main():
    person = {"name": "Ali",
              "age": 25,
              "city": "Tashkent"
}
    del person["city"]

    console.print(person ,style = 'blink yellow')

main()