from rich.console import Console

console = Console()

def main():
    settings = {
        'mode':'dark',
        'volume':70 ,
    }

    settings.clear()

    console.print(settings,style = 'bold cyan')

main()