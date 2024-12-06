# Step 1: Open the log file and read lines
with open("sample.log", "r") as file:  
    lines = file.readlines()

# Step 2: Initialize an empty dictionary to store endpoint counts
endpoint_counts = {}

# Step 3: Loop through each line to extract endpoints
for line in lines:
    # Extract the part inside the quotes containing the HTTP method and endpoint
    parts = line.split('"')
    if len(parts) > 1:  # Ensure the line has the expected structure
        request = parts[1]  # The part with the HTTP method and endpoint
        endpoint = request.split()[1]  # Extract the endpoint (second part)
        
        # Step 4: Update the count in the dictionary
        if endpoint in endpoint_counts:
            endpoint_counts[endpoint] += 1  # Increment count if endpoint already in dictionary
        else:
            endpoint_counts[endpoint] = 1   # Add endpoint to dictionary with a count of 1

# Step 5: Sort the dictionary by count in descending order
sorted_endpoints = sorted(endpoint_counts.items(), key=lambda item: item[1], reverse=True)

# Step 6: Print the sorted endpoints and their counts
print(f"{'Endpoint':<20}{'Request Count'}")
for endpoint, count in sorted_endpoints:
    print(f"{endpoint:<20}{count}")

# Step 7: Identify the most frequent endpoint
most_frequent_endpoint = sorted_endpoints[0] if sorted_endpoints else None
if most_frequent_endpoint:
    print("\nMost Frequent Endpoint:")
    print(f"{most_frequent_endpoint[0]} with {most_frequent_endpoint[1]} requests")




