from rich.console import Console

console = Console()

def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    group = {}
    for student in students:
        group.setdefault(student['group'],[]).append(student['name'])

    return group

students = [
    {
        "name":"ali", 
        "group": "A"
    },
    {
        "name":"vali", 
        "group": "B"
    },
    {
        "name":"sami", 
        "group": "A"
    },
    {
        "name":"gani", 
        "group": "A"
    },

]
group = group_students(students)
console.print(group,style = 'bold red')