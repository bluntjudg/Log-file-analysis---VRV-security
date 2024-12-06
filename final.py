import csv
with open("sample.log", "r") as file:
    lines = file.readlines()

ip_counts = {}

for line in lines:
    ip = line.split()[0]

    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

sorted_ips = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)

print(f"{'IP address': <20}{'request count'}")
for ip, count in sorted_ips:
    print(f"{ip:<20}{count}")

print("   ")
#step 2:
endpoints_counts = {}

for line in lines:
    parts = line.split('"')
    if len(parts) > 1:
        request = parts[1]
        endpoint = request.split()[1]

    if endpoint in endpoints_counts:
        endpoints_counts[endpoint] += 1
    else:
        endpoints_counts[endpoint] = 1

sorted_endpoints = sorted(endpoints_counts.items(), key=lambda item: item[1], reverse=True)

print(f"{'Endpoints': <15}{'Request count'}")
for endpoints, count in sorted_endpoints:
    print(f"{endpoints:<20}{count}")

frequent_endpoints = sorted_endpoints[0] if sorted_endpoints else None
if frequent_endpoints:
    print("most frequent endpoints are:")
    print(f"{frequent_endpoints[0]} - {frequent_endpoints[1]} requests")

print("  ")
'''

#step 3:  find out why this is different from this code 
failed_attempts = {}

for line in lines:
    if "401" in line or "Invalid Credentials" in line:
        ip = line.split()[0]

    if ip in failed_attempts:
        failed_attempts[ip] += 1
    else:
        failed_attempts[ip] = 1
#print("Failed attempts dictionary:", failed_attempts)

Threshold = 7

print(f"{'suspecious IP':<20}{'failed attempts'}")
for ip, count in failed_attempts.items():
    if count > Threshold:
        print(f"{ip:<20}{count}")
'''
#step 3 : correct one {why different from above}
failed_attempts = {}

for line in lines:
    if "401" in line or "Invalid Credentials" in line:
        ip = line.split()[0]  # Extract the IP for each failed login attempt

        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1

# Print the suspicious IPs that exceed the threshold
Threshold = 3
print(f"{'Suspicious IP':<20}{'Failed attempts'}")
for ip, count in failed_attempts.items():
    if count > Threshold:
        print(f"{ip:<20}{count}")


#step 4
with open("log_analysis.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write Requests per IP
    csv_writer.writerow(["Requests per IP"])
    csv_writer.writerow(["IP Address", "Request Count"])
    for ip, count in sorted_ips:
        csv_writer.writerow([ip, count])
    
    csv_writer.writerow([])  # Blank row for separation
    
    # Write Most Accessed Endpoints
    csv_writer.writerow(["Most Accessed Endpoints"])
    csv_writer.writerow(["Endpoint", "Access Count"])
    for endpoint, count in sorted_endpoints:
        csv_writer.writerow([endpoint, count])

    
    csv_writer.writerow([])  # Blank row for separation
    
    # Write Suspicious Activity
    csv_writer.writerow(["Suspicious Activity"])
    csv_writer.writerow(["IP Address", "Failed Login Count"])
    for ip, count in failed_attempts.items():
        csv_writer.writerow([ip, count])

print("\nResults have been saved to 'log_analysis.csv'.")


         
