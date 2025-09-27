from rich.console import Console

console = Console()

def most_common_char(text: str) -> str:
    mx = text[0]
    for ch in text:
        if text.count(ch) > text.count(mx):
            mx = ch 

    return mx 

text = "fygbdydufergbcisehohwsjbsdhchafihuie hcuiwehifergfawdgf"
most_ch = most_common_char(text)
console.print(most_ch,style = 'italic magenta')