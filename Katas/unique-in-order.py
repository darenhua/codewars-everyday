def unique_in_order(iterable):
    list = []
    for i in iterable:
        if len(list) < 1 or not i == list[len(list) - 1]:
            list.append(i)
    return list
