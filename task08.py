from rich.console import Console

console = Console()

def main():
    user = {
    "name": "Ali",
    "email": "noto'g'ri_email",
    "age": 30
}
    
    user['email'] = 'correct@email.com'

    console.print(user,style = 'red')

main()
