print("Welcome to the Timezone Calculator")

timezones = {
    "ET": 5,
    "CT": 6,
    "MT": 7, 
    "PT": 8, 
}

current_timezone = input("Enter your current timezone abbreviation:").upper()
desired_timezone = input("Enter your desired timezone abbreviation:").upper()
current_time = input("Enter your current time in military time:")

total_min = 0
if len(current_time) == 5:
    current_hour = int(current_time[0:2])
    current_min = int(current_time[3:5])
    total_min = (current_hour * 60) + current_min
elif len(current_time) == 4:
    current_hour = int(current_time[0:1])
    current_min = int(current_time[2:4])
    total_min = (current_hour * 60) + current_min
    
#convert to UTC
#subtract the time
# then convert to desired time by adding from UTC

def converting():
    subtract_value = 60
    UTC_time = total_min - subtract_value
    add_value = 0
    desired_time_min = UTC_time + add_value
    desired_time_hour = desired_time_min/60
    return desired_time_hour

print("Converting Your Time...")
print(converting())

# for timezone in timezones
# user input (ET)
# pythons find def ET => whats in def ET
#.(count) >0 