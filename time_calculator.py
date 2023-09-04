def add_time(start, duration, day = ""):
  for start_time in start:
    parts = start.split()
    parts1 = parts[0].split(":")
    hours = parts1[0]
    minutes = parts1[1]
    day_time = parts[1]
   # print(hours, minutes, day_time)
    
    for duration_time in duration:
      parts2 = duration.split()
      parts3 = parts2[0].split(":")
      dur_hours = parts3[0]
      dur_minutes = parts3[1]
     # print(dur_hours, dur_minutes)
      
      day_counter = 0
      new_hours = int(hours) + int(dur_hours)
      new_minutes = int(minutes) + int(dur_minutes)
      week_days = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

      if new_hours > 12 and day_time == "AM":
        new_hours = new_hours - 12
        new_day_time = "PM"
      if new_hours > 12 and day_time == "PM":
        new_hours = new_hours - 12
        new_day_time = "AM"
        day_counter = day_counter + 1
        #print(day_counter)
      if new_minutes > 60:
        new_hours = new_hours + 1
        new_minutes = new_minutes - 60

      if day.lower() in week_days:
        if day_counter >= 1:
          x = week_days.index(day.lower()) 
          y = x + day_counter
          new_day = week_days[y]
          new_time = str(new_hours)+ ":" + str(new_minutes)+ " " + new_day_time + ", " + new_day.capitalize() 
      elif day_counter >= 1 :
        new_time = str(new_hours)+ ":" + str(new_minutes)+ " " + new_day_time + " (next day)"
      elif day_counter > 1:
        new_time = str(new_hours)+ ":" + str(new_minutes)+ " " + new_day_time + " (" + day_counter + "days later)"
      else:
        new_time = str(new_hours)+ ":" + str(new_minutes)+ " " + new_day_time 
    
    return new_time
