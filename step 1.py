# Step 1: Open the log file and read lines
with open("sample.log", "r") as file:  
    lines = file.readlines()

# Step 2: Initialize an empty dictionary to store counts
ip_counts = {}

# Step 3: Loop through each line to extract IP addresses
for line in lines:
    # Split the line by spaces and get the first part (the IP address)
    ip = line.split()[0]
    
    # Step 4: Update the count in the dictionary
    if ip in ip_counts:
        ip_counts[ip] += 1  # Increment count if IP already in dictionary
    else:
        ip_counts[ip] = 1   # Add IP to the dictionary with a count of 1

# Step 5: Sort the dictionary by count in descending order
sorted_ips = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)

# Step 6: Print the results in descending order
print(f"{'IP Address':<15}{'Request Count'}")
for ip, count in sorted_ips:
    print(f"{ip:<20}{count}")

