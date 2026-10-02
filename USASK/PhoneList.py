NumOfTestCases = int(input())

for _ in range(NumOfTestCases):
    n = int(input())
    numbers = []

    for _ in range(n):
        numbers.append(input().strip())

    numbers.sort()
    # key idea: string sorting! it checks each char one by one, and if my first > your first, the rest and length does not matter
    # but in this case, if a phone number is a prefix of another, it must be at the front just before that!
    consistent = True
    for i in range(n-1):
        if numbers[i+1].startswith(numbers[i]):
            consistent = False
            break
        
        
    if consistent:
        print("YES")
    else:
        print("NO")