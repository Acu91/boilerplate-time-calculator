def add_time(start, duration, day=""):
 
  #Definition of variables
  dayafter=0
  new_time=""
  N_day=0


  #Extract data for string. 
  #S_ stand for Start
  #D_ stand for Duration
  #N_ stand for number of
  S_hour = int(start[0:start.find(':')])
  S_minutes = int(start[start.find(':')+1:start.find(" ")])
  S_AmPm = (start[start.find(" ")+1:])
  
  D_hour = int(duration[0:duration.find(':')])
  D_minutes = int(duration[duration.find(':')+1:])

  N_minutes = S_minutes + D_minutes
  N_hour = S_hour + D_hour

  #Test if minute is greater of 60min
  if N_minutes > 60:
    N_minutes = N_minutes - 60
    N_hour = N_hour + 1
    
  #Test if Hour are greater than 24
  if N_hour/24 > 1:
    dayafter=int(N_hour/24)
    N_hour=N_hour-24*(int(N_hour/24))
    if N_hour > 12:
      N_hour = N_hour - 12
      if S_AmPm == "AM":
        S_AmPm = "PM"
      else:
        S_AmPm = "AM"
        dayafter=dayafter + 1
    elif N_hour==12:
      N_hour=12
      if S_AmPm == "AM":
        S_AmPm = "PM"
      else:
        S_AmPm = "AM"
        dayafter=dayafter + 1
  elif N_hour > 12:
      N_hour = N_hour - 12
      if S_AmPm == "AM":
        S_AmPm = "PM"
      else:
        S_AmPm = "AM"
        dayafter=dayafter + 1
  elif N_hour==12:
    N_hour=12
    if S_AmPm == "AM":
      S_AmPm = "PM"
    else:
      S_AmPm = "AM"
      dayafter=dayafter + 1  
  
  #Define the day of the week
      
  if day!="":      
    if day=="Monday":
      N_day=1
    elif day=="Tuesday":
      N_day=2
    elif day=="Wednesday":
      N_day=3
    elif day=="Thurstday":
      N_day=4
    elif day=="Friday":
      N_day=5
    elif day=="Saturday":
      N_day=6
    elif day=="Sunday":
      N_day=7
    
  N_day=N_day+dayafter

  
  if N_day/7>1:
    N_day=N_day-7*int(N_day/7)
    if N_day > 7:
      N_day=N_day-7

  #Assign day of the week
      
  if day!="":
    if N_day == 1:
      day="Monday"
    elif N_day==2:
      day="Tuesday"
    elif N_day==3:
      day="Wednesday"
    elif N_day==4:
      day="Thurstday"
    elif N_day==5:
      day="Friday"
    elif N_day==6:
      day="Saturday"
    elif N_day==7:
      day="Sunday"

  #Set the new time
  
  if day == "":
    if dayafter==0:
      new_time = str(N_hour) + ":" + str(N_minutes).rjust(2,"0") + " " + S_AmPm
    elif dayafter==1:  
      new_time = str(N_hour) + ":" + str(N_minutes).rjust(2,"0") + " " + S_AmPm + " " + "(next day)"
    elif dayafter>1:
      new_time = str(N_hour) + ":" + str(N_minutes).rjust(2,"0") + " " + S_AmPm + " " + "(" + str(dayafter) + " days later)"
  else:
    if dayafter==0:
      new_time = str(N_hour) + ":" + str(N_minutes).rjust(2,"0") + " " + S_AmPm + ", " + day
    elif dayafter==1:  
      new_time = str(N_hour) + ":" + str(N_minutes).rjust(2,"0") + " " + S_AmPm + ", " + day + " (next day)"
    elif dayafter>1:
      new_time = str(N_hour) + ":" + str(N_minutes).rjust(2,"0") + " " + S_AmPm + ", " + day + " (" + str(dayafter) + " days later)"
  
  return new_time
