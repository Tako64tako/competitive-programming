N = int(input())
people = []
result = []
for _ in range(N):
    name, age = input().split()
    age = int(age)
    people.append((name, age))

min_people = min(people, key=lambda x: x[1])
min_index = people.index(min_people)

for _ in people[min_index:]:
    result.append((_[0], _[1]))
for _ in people[:min_index]:
    result.append((_[0], _[1]))

for _ in result:
    print(_[0])