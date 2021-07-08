print("Welcome to the Timezone Calculator")

timezones = {
    "UTC": 0,
    "ET": -5,
    "CT": -6,
    "MT": -7, 
    "PT": -8, 
    "AK": -9, 
    "HAST": -10, 
    "KST": 9,
}
print(f"Here are the timezone options {timezones.keys()}")
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

def converting():
    subtract_value = int(timezones.get(current_timezone)) * 60
    UTC_time = total_min - subtract_value
    if UTC_time < 0:
        return "unresolved error come back later please D:"
    else: 
        add_value = int(timezones.get(desired_timezone)) * 60
        total_time_min = UTC_time + add_value
        desired_time_hour = int(total_time_min/60)
        if(desired_time_hour >= 24):
            desired_time_hour -= 24
        # elif (desired_time_hour < 0):
        #     desired_time_hour -= 24
        desired_time_min = int(total_time_min % 60)
        final_time = f"{desired_time_hour}:{desired_time_min}"
        return final_time

print("Converting Your Time...")
print(converting())
