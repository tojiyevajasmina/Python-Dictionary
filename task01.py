from rich.console import Console

console = Console()

def main():
 student = {}

 student['name'] = 'JASMINA'
 student['age'] = 18
 student['grade'] = '11-B'

 console.print (student, style ="italic green" )

main()

