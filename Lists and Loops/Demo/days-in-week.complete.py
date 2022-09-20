# Make a list of the weekdays
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Make a list of the weekend days
weekend = ["Saturday", "Sunday"]

# Print all the weekdays
for day in weekdays:
    print(day)

print("-----------------")
# Combine the lists into daysOfWeek
daysOfWeek = weekdays + weekend

# Print all the days of the week
for day in daysOfWeek:
    print(day)

print("-----------------")
# Print daysOfWeek[5] - It should be Saturday
print(daysOfWeek[5])

print("-----------------")
# Change Saturday to Caturday
daysOfWeek[5] = "Caturday"

# Add a new day to the week called Funday
daysOfWeek.append("Funday")

# Print all 8 days
for day in daysOfWeek:
    print(day)

print("-----------------")
# Delete Mondays (for Garfield)
daysOfWeek.pop(0)

# Print improved days of week
for day in daysOfWeek:
    print(day)

print("-----------------")
# Print each letter in Caturday (now index 4)
for letter in daysOfWeek[4]:
    print(letter)

print("-----------------")
print("-----------------")
# Print each letter in each day
for day in daysOfWeek:
    for letter in day:
        print(letter)
    
    print("-----------------")