from rich.console import Console

console = Console()

def main():
        data = {
    "name": "JASMINA",
    "age": 18,
    "city": "SAMARQAND"
    }
        
        for key, value in data.items():
         console.print(f"{key.upper()} → {value}",style = 'italic white')

main()