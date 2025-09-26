from rich.console import Console

console = Console()

def main():
    scores = {"math": 90, 
              "english": 85, 
              "science": 92
}

    total = 0
    for value in scores.values():
      total += value  

    console.print(total, style = 'italic yellow')

main()