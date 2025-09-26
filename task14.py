from rich.console import Console

console = Console()

def main():
    person = {"name": "Ali",
               "age": 25, 
               "city": "Tashkent"
}

    s = person.pop("age")

    console.print(s,style = 'strike magenta')

main()