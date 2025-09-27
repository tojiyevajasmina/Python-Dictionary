from rich.console import Console 

console = Console()

def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    filtered_dict = {}
    for key, value in d.items():
        if value != 0:
            filtered_dict[key] = value
    return filtered_dict

sample_dict = {
    "a": 10,
    "b": 0,
    "c": 5,
    "d": 0,
    "e": 7
}

result = filter_non_zero(sample_dict)

console.print(result, style = 'bold green')