NumOfTestCases = int(input())

for _ in range(NumOfTestCases):
    n = int(input())
    numbers = []

    for _ in range(n):
        numbers.append(input().strip())

    numbers.sort()
    # key idea: string sorting! for shorter one always comes first, and one by one checking 
    consistent = True
    for i in range(n-1):
        if numbers[i+1].startswith(numbers[i]):
            consistent = False
            break
        
        
    if consistent:
        print("YES")
    else:
        print("NO")