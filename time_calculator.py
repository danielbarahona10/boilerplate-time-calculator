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

  # Hours of the duration
  duration_hour = int(duration.split(":")[0])
  # Minutes of the duration
  duration_minute = int(duration.split(":")[1])

  # Calculate the new time
  new_minute = (start_minute + duration_minute)%60
  new_hour = (start_hour + duration_hour + (start_minute + duration_minute)//60)%12

  # Format the new time
  new_time = f'{new_hour:02d}' + ":" + f'{new_minute:02d}' + " " + am_pm
  
  return new_time