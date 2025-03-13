def add_time(start, duration, day=''):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    current = start.split(' ')
    currentTimes = current[0].split(':')
    addTimes = duration.split(':')
    new_days = 0
    new_indicator = current[1]
    new_hour = int(currentTimes[0]) + int(addTimes[0])
    new_minute = int(currentTimes[1]) + int(addTimes[1])
    check_hour = 0

    # add minutes
    if new_minute > 60:
        new_hour += 1
        new_minute = new_minute - 60

    if new_hour >= 12:
        # calculate new days
        if current[1] == 'PM':
            check_hour = new_hour % 12
            new_days = 1 + int(new_hour / 24)
        else:
            check_hour = new_hour % 24
            if new_hour >= 24:
                new_days = int(new_hour / 24)

        # calculate time indicator and new hour
        if check_hour >= 12:
            new_indicator = 'PM'
        else:
            new_indicator = 'AM'
        new_hour = 12 if new_hour % 12 == 0 else new_hour % 12

    # calculate day name
    for i in range(len(days)):
        if day.lower() == days[i].lower():
            if day != '' and new_days / 7 != 0:
                day = ', ' + days[(i + new_days) % 7]
                break
            else:
                day = ', ' + days[i]
                break

    # prepare return date string
    time_indicator = ''
    if new_days == 1:
        time_indicator = ' (next day)'
    elif new_days > 1:
        time_indicator = ' (' + str(new_days) + ' days later)'
    new_minute_str = '0' + str(new_minute) if new_minute < 10 else str(new_minute)
    new_time = str(new_hour) + ":" + new_minute_str + ' ' + new_indicator + day + time_indicator

    print(new_time)

    return new_time

# test cases
add_time('3:30 AM', '2:12')
add_time('6:50 PM', '103:00')
add_time('11:59 AM', '42:09', 'thursday')