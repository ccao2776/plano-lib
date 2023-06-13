

start_time = "11.00"
end_time = "1.00"

def time_to_attr(time):
    time = str(time).split(".")

    hour = time[0]
    minutes = time[1]

    if len(minutes) == 1:
        minutes = minutes + "0"

    return hour + ":" + minutes + " pm"

def increment_time(time):
    time = str(time).split(".")

    hour = int(time[0])
    minutes = int(time[1]) + 15
    
    if minutes == 60:
        hour = hour + 1
        minutes = 0
    
    if hour > 12:
        hour = 1
    
    return str(hour) + "." + str(minutes)

for i in range(0, 10):
    print(time_to_attr(start_time), time_to_attr(end_time))
    start_time = increment_time(start_time)
    end_time = increment_time(end_time)