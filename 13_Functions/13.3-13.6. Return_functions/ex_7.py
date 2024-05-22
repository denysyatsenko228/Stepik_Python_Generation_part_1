"""
Merge lists 2
На вход программе подается число n, а затем n строк, содержащих целые числа в
порядке возрастания. Из данных строк формируются списки чисел. Напишите программу,
которая объединяет указанные списки в один отсортированный список с помощью
функции quick_merge(), а затем выводит его.
"""


def quick_merge(lines):
    merged_list = []
    for line in lines:
        merged_list.extend(line.split())

    int_list = [int(i) for i in merged_list]
    return sorted(int_list)


n = int(input())
lines = []
for _ in range(n):
    line = input()
    lines.append(line)

res = quick_merge(lines)
print(*res)
