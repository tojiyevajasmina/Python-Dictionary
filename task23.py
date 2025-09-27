from rich.console import Console
console = Console()

def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = dict()
    for i, num in enumerate(numbers):
        group.setdefault(num,[]).append(i)

    return group

nums = [1,2,3,4,5,3,2,6,7,8,8,7,6,5,4,8,9,2,8]
result = group_indices(nums)
console.print(result,style = 'italic yellow')