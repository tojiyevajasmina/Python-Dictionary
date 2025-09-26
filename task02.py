from rich.console import Console

console = Console()

def main():
    book = {
        'title': "Python Basics",
        'author': "Diyorbek Jumanov",
        'pages': 250
  }

    console.print(book ,style = "bold red")

main()