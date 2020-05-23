# Enter your code here. Read input from STDIN. Print output to STDOUT

numTestCases = input()
inputs = [input() for i in range(int(numTestCases))]


for i in inputs:
    evens = []
    odds = []
    for count, char in enumerate(i):
        if count % 2 == 0:
            evens.append(char)
        elif count % 2 != 0:
            odds.append(char)
    evenStr = ''.join(evens)
    oddStr = ''.join(odds)
    print(evenStr, oddStr)
