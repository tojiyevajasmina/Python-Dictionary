from rich.console import Console
console = Console()

def count_names(name: list[str])-> dict[str ,int]:
    result = {}
    for name in names:
        if name not in result.keys():
            result[name] = names.count(name)
        
    return result

names = ['ali','vali','gani','sami','ali', 'sami','ali','gani','gani']

result = count_names(names)
console.print(result,style = 'italic green')