from rich.console import Console

console = Console()

def main():
    student = {"name": "Ali", "age": 25, "grade": "A"}

    for key , value in student.items():
     console.print(key, value, style = "italic red")

main()