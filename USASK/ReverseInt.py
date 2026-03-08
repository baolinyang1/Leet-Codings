x = input()
if x[0] == "-":
    result = ["-"]
    for i in range(len(x)-1,0,-1):
        result.append(x[i])
    final = "".join(result)
    if int(final) < -(2**31):
        print(0)
    else:
        print(final)

else:
    result = []
    for i in range(len(x)-1,-1,-1):
        result.append(x[i])
    final = "".join(result)
    if int(final) > (2**31 - 1):
        print(0)
    else:
        print(final)