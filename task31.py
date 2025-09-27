from rich.console import Console 

console = Console()

def count_letters(text: str) -> dict[str, int]:
    counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

text = "assalomu alaykum"
result = count_letters(text)

console.print(result,style = 'italic green')