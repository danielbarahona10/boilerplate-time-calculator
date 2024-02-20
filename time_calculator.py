def add_time(start, duration, start_day = "Monday"):
  # New time string
  new_time = ""
  # Split start time into the time and AM/PM
  start_time = start.split()
  # Hour of the start time
  start_hour = int(start_time[0].split(":")[0])
  # Minute of the start time
  start_minute = int(start_time[0].split(":")[1])
  # AM/PM of the start time
  am_pm = start_time[1]

  # Absolute minutes of the start time
  if am_pm == "AM":
    start_abs_minutes = start_hour * 60 + start_minute
  else:
    start_abs_minutes = (start_hour+12) * 60 + start_minute
  
  # Hours of the duration
  duration_hour = int(duration.split(":")[0])
  # Minutes of the duration
  duration_minute = int(duration.split(":")[1])

  # Absolute minutes of the duration
  duration_abs_minutes = duration_hour * 60 + duration_minute
  
  # Number of days later
  days_later = (start_abs_minutes + duration_abs_minutes) // (24*60)
  
  # Calculate the new time
  new_minute = (start_minute + duration_minute)%60
  new_hour = (start_hour + duration_hour + (start_minute + duration_minute)//60)%12

  # Format the new time
  if days_later == 0:
    new_time = f'{new_hour:02d}' + ":" + f'{new_minute:02d}' + " " + am_pm
  elif days_later == 1:
    new_time = f'{new_hour:02d}' + ":" + f'{new_minute:02d}' + " " + am_pm + " (next day)"
  else:
    new_time = f'{new_hour:02d}' + ":" + f'{new_minute:02d}' + " " + am_pm + " (" + str(days_later) + " days later)"
  
  return new_time