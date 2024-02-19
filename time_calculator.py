def add_time(start, duration, start_day = "Monday"):
  new_time = ""
  start_time = start.split()
  start_hour = int(start_time[0].split(":")[0])
  start_minute = int(start_time[0].split(":")[1])
  am_pm = start_time[1]
  
  duration_hour = int(duration.split(":")[0])
  duration_minute = int(duration.split(":")[1])

  new_minute = (start_minute + duration_minute)%60
  new_hour = (start_hour + duration_hour + (start_minute + duration_minute)//60)%12

  new_time = f'{new_hour:02d}' + ":" + f'{new_minute:02d}' + " " + am_pm
  
  return new_time