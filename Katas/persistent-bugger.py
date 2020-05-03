def persistence(n):
    number = str(n)
    num = 1
    count = 0 
    while len(number) > 1:
        for i in number:
            num *= int(i)
        number = str(num)
        num = 1
        count += 1
    return count

print(persistence(39))
