# the number of hours worked in a week
hours_worked = input("Enter the number of hours worked this week: ")

# Convert hours worked to a floating-point number
hours_worked = float(hours_worked)

# Determine regular hours and overtime hours
if hours_worked > 40:
  regular_hours = 40
  overtime_hours = hours_worked - 40
else:
  regular_hours = hours_worked
  overtime_hours = 0

# Calculate regular pay and overtime pay
regular_pay = regular_hours * 20
overtime_pay = overtime_hours * 30

# Calculate total pay
total_pay = regular_pay + overtime_pay

# Display the total pay
print("Total pay: $" + str(total_pay))

