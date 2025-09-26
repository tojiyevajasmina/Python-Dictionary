from rich.console import Console

console = Console()

def main():
    config = {}

    for i in range(3):
      key = input(f"{i+1}->: setting nomini kiriting: ")
      value = input(f"{i+1}->: {key} uchun qiymat kiriting: ")
      config[key] = value

    console.print(config,style = 'green')

main()