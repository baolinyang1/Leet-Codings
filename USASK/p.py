N = int(input())
Socks = []
for i in range(N):
    type, fit, number = input().split()
    number = int(number)
    Socks.append((type, fit, number))

typecounter = {}
for i in Socks:
    print(i)
    if i[0] not in typecounter and i[1] != 'any':
        typecounter[i[0]] = 1
    elif i[0] in typecounter and i[1] != 'any':
        typecounter[i[0]] = 2
    elif i[0] not in typecounter and i[1] == 'any' and i[2] >= 2:
        typecounter[i[0]] = 3
    elif i[0] not in typecounter and i[1] == 'any' and i[2] == 1:
        typecounter[i[0]] = 4

print(typecounter)

result = 0
resultkeys = [k for k,v in typecounter.items() if v == 1 or v == 4]
yesforany = [k for k,v in typecounter.items() if v == 3]
for i in Socks:
    if i[0] in resultkeys:
        result += i[2]

Socksbackup = []
socksthathavebothpairskey = [k for k,v in typecounter.items() if v == 2]
maxi = 0
for i in Socks:
    if i[0] in socksthathavebothpairskey and i[2] > maxi:
        maxi = i[2]

result2=maxi + 1

result1 = 2 if len(yesforany)==1 else 0

final = max(result+result1, result+result2)
print(final)

# if yesforany:
#     print(result + 2)
# elif:

    
# final results === sum of all the names that have value 1 + sum of all value 4s + (...)



# findMax = False
# result = 0
# for i in range(len(Socks) - 1, -1, -1):
#     if Socks[i][1] != 'any':
#         FindMax = True
#         result += Socks[i][2]
#         break

# for i in Socks:
#     if i[1] == 'any' and i[2] >= 2:
#         print(result + 2)
#     if i[1] == 'any' and i[2] == 1:
#         result += 1
    

