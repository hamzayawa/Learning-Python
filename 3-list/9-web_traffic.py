traffic_data = [150, 180, 300, 400, 600, 800, 900, 700, 500, 350, 200, 150]

# Get the peak traffic hours (the top 3 hours)
peak_traffic_hours = sorted(range(len(traffic_data)), key=lambda i: traffic_data[i], reverse=True)[:3]

# Get the average traffic for the day (excluding the first and last hour)
average_traffic = sum(traffic_data[1:-1]) / (len(traffic_data) - 2)

# Print the results
print(f"Peak traffic hours: {peak_traffic_hours}")
print(f"Average traffic: {average_traffic}")
