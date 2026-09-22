def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None


lista = ["Python", "Java", "C++", "JavaScript"]

print(get_item(lista, 1))
print(get_item(lista, 10))