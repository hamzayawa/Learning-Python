# Set initial variables
savings = 1000
interest_rate = 0.05
years = 0

# Set savings goal
goal = 2000

# Calculate compound interest until goal is reached
while savings < goal:
    years += 1
    interest = savings * interest_rate
    savings += interest

# Output results
print(f"It took {years} years to save ${goal:.2f}")
