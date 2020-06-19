# 리뉴얼 코드
import datetime

def solution(a, b):
    d = datetime.datetime(2016, a, b)
    weekdays = {'Sunday':'SUN', 'Monday':'MON', 'Tuesday':'TUE', 'Wednesday':'WED',
                'Thursday':'THU', 'Friday':'FRI', 'Saturday':'SAT'}
    answer = d.strftime('%A')
    return weekdays.get(answer)

# 제출코드
import datetime

def solution(a, b):
    d = datetime.datetime(2016, a, b)
    weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    answer = d.strftime('%A')
    
    if answer == 'Sunday': return weekdays[0]
    elif answer == 'Monday': return weekdays[1]
    elif answer == 'Tuesday': return weekdays[2]
    elif answer == 'Wednesday': return weekdays[3]
    elif answer == 'Thursday': return weekdays[4]
    elif answer == 'Friday': return weekdays[5]
    elif answer == 'Saturday': return weekdays[6]