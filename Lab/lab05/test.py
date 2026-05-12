lst = [1, 2, 3]
it = iter(lst)
for i in it:
    if i == 2:
        break
print(list(it).__reversed__)
print(list(it))