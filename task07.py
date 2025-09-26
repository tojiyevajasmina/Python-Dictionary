from rich.console import Console

console = Console()

def main():
    person = {"name": "Ali",
              "age": 25, 
              "city": "Tashkent"
}

    person ["age"] = 26

    console.print(person ,style = 'underline blue')

main()