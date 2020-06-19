month, day = map(int, input().split())

day_of_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

for i in range(1, month):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        day += 31
    elif i in [4, 6, 9, 11]:
        day += 30
    else:
        day += 28

print(day_of_week[(day % 7) - 1])