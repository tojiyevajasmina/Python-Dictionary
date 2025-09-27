def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    group = {}
    for person in people:

        group.setdefault(person['group'],[]).append(persons['name'])


    return group


persons = [
    {
        "name": "ali",
        "age": 12
    },
    {
        "name": "vali",
        "age": 14
    },
    {
        "name": "gani",
        "age": 12
    },
    {
        "name": "smai",
        "age": 19
    },
]

group = group_by_age(persons)
print(persons)