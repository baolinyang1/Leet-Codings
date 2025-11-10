m, p, n = map(int, input().split())
Percent = p / 100

workTimes = []
Goals = [m]
currentGoal = m
# store the first n day's of working minutes in a list
for i in range(0, n):
    num = int(input())
    workTimes.append(num)
    if i != n -1:
        nextGoal = (currentGoal - num) * Percent + m
        Goals.append(nextGoal)
        currentGoal = nextGoal

Counter = 0
for i in range(0, len(workTimes)):
    if workTimes[i] - Goals[i] > 0:
        Counter += 1

print(Counter)
    


