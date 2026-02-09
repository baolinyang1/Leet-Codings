t = int(input())

for _ in range(t):
    words = input().split()

    sounds_to_remove = set()

    line = input().strip()
    while line != "what does the fox say?":
        parts = line.split()          # "<animal> goes <sound>"
        sounds_to_remove.add(parts[2])
        line = input().strip()

    result = [w for w in words if w not in sounds_to_remove]
    print(" ".join(result))

        


