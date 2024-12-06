# Step 1: Open the log file and read lines
with open("sample.log", "r") as file:  
    lines = file.readlines()

# Step 2: Initialize an empty dictionary to store failed login counts
failed_attempts = {}

# Step 3: Loop through each line to detect failed login attempts
for line in lines:
    if "401" in line or "Invalid credentials" in line:  # Check for failure indicators
        ip = line.split()[0]  # Extract the IP address
        # Step 4: Update the count in the dictionary
        if ip in failed_attempts:
            failed_attempts[ip] += 1  # Increment count if IP already in dictionary
        else:
            failed_attempts[ip] = 1   # Add IP to dictionary with a count of 1


#print("Failed attempts dictionary:", failed_attempts)

# Step 5: Define a threshold for suspicious activity
threshold = 5  # Adjust the threshold as needed

# Step 6: Identify and display suspicious IPs
print(f"\n{'Suspicious IP':<20} {'Failed Attempts'}")
for ip, count in failed_attempts.items():
    if count > threshold:  # Flag IPs exceeding the threshold
        print(f"{ip:<20}{count}")
