def add_time(start, duration, day="none"):
    #Splits arguments into hours/min/period
    sTime = start.split(":")
    sHour = int(sTime[0])
    sMin = int((sTime[1]).split()[0])
    period = (sTime[1]).split()[1]
    aTime = duration.split(":")
    aHour = int(aTime[0])
    aMin = int((aTime[1]).split()[0])
    daysLater = 0

    #if new minutes > 60
    newMin = sMin + aMin
    if newMin > 59:
        aHour += 1
        newMin -= 60
    #If min is a single digit, adds 0 in front
    if len(str(newMin)) == 1:
        newMin = str(newMin).rjust(2, "0")
    
    newHour = sHour + aHour
    #if new hour > 24
    if newHour > 24:
        daysLater = int(newHour / 24)
        newHour %= 24

    #if new hour > 11 hours (switch period)
    if newHour > 11:
        if period == "AM": 
            period = "PM"
        elif period == "PM": 
            period = "AM"
            daysLater += 1 #Switching from PM -> AM = next day

    #if new hour > 12 hours (subtract 12, bc of 12 hour system)
    if newHour > 12:
        newHour -= 12

    #list of days of the week
    dayOfWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = day.lower() #Standardizes user input to be lowercase 

    #if day of the week, find index in list, add how many days have passed mod 7, convert back to day
    if day in dayOfWeek:
        num = dayOfWeek.index(day)
        num = (daysLater + num) % 7
        day = dayOfWeek[num]

    #Create string to be returned, if optional arg day given
    if day != "none":    
        if daysLater == 0:
            new_time = str(newHour) + ":" + str(newMin) + " " + period + ", " + day.capitalize()
        elif daysLater == 1:
            new_time = str(newHour) + ":" + str(newMin) + " " + period + ", " + day.capitalize() + " (next day)" 
        elif daysLater > 1:
            new_time = str(newHour) + ":" + str(newMin) + " " + period + ", " + day.capitalize() + " (" + str(daysLater) + " days later)" 
    #Create string to be returned, if optional arg day NOT given
    else:
        if daysLater == 0:
            new_time = str(newHour) + ":" + str(newMin) + " " + period
        elif daysLater == 1:
            new_time = str(newHour) + ":" + str(newMin) + " " + period + " (next day)" 
        elif daysLater > 1:
            new_time = str(newHour) + ":" + str(newMin) + " " + period + " (" + str(daysLater) + " days later)" 
    return new_time

print(add_time("9:15 PM", "33335:30", "mONday"))