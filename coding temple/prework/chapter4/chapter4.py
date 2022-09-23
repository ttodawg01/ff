foods= ['pizza', 'tacos', 'dim sum', 'sushi', ]
print(foods[1])
for food in foods:
    print(f"I like {food} because they are yummy")


print(list(range(4)))
my_list= [1, 3.0, ["a", "b", ["A", "B", "C"], 'd'], "john"]
for member in my_list:
    if isinstance(member, list):
        for m in member:
            if isinstance(m, list):
                print(m, end=" ")