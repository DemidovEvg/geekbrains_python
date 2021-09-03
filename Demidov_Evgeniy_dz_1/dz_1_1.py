duration = int(input("Please, enter time in seconds: "))

seconds_name = 'сек'
minutes_name = 'мин'
hours_name = 'час'
days_name = 'дн'

time_segments = ((seconds_name, 60), (minutes_name, 60), (hours_name, 60), (days_name, 365))

time_with_days = {}

for time_name, time_value in time_segments:
    if time_name == days_name:
        time_with_days[time_name] = duration
        break
    else:
        time_with_days[time_name] = duration % time_value
        duration //= time_value
        if duration == 0:
            break
result = ''

for time_segment in reversed(time_with_days):
    result += f'{time_with_days[time_segment]} {time_segment} '

print(result)
