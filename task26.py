from rich.console import Console

console = Console()

def merge_dicts(a: dict, b: dict) -> dict:
    merged = {}

    for key in a:
        merged[key] = a[key]

    
    for key in b:
        merged[key] = b[key]
    return merged

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}

result = merge_dicts(a, b)

console.print(result, style='bold cyan')

