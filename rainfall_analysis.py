# Initialize variables
valid_days = 0
rainy_days = 0
total_rainfall = 0.0
max_rainfall = 0.0

print("Enter daily rainfall amounts. Use 9999 to terminate.")

while True:
    try:
        # Read input
        rainfall = float(input("Enter rainfall (mm): "))
        
        # Check for sentinel value
        if rainfall == 9999:
            break
        
        # Reject invalid (negative) rainfall values
        if rainfall < 0:
            print("Invalid input. Rainfall cannot be negative.")
            continue

        # Accumulate valid statistics
        valid_days += 1
        total_rainfall += rainfall

        if rainfall > 0:
            rainy_days += 1
        
        # Check for maximum rainfall
        if rainfall > max_rainfall:
            max_rainfall = rainfall

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Output results
print("\n---- Rainfall Statistics ----")
print(f"Number of valid recorded days: {valid_days}")
print(f"Number of rainy days: {rainy_days}")
print(f"Total rainfall: {total_rainfall} mm")
print(f"Maximum rainfall in a day: {max_rainfall} mm")
