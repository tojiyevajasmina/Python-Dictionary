from rich.console import Console

console = Console()

def main():
    person = {"name": "Ali", "age": 25}

    person['email'] = "ali@example.com"

    console.print(person,style = 'italic yellow')

main()