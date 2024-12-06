**Log Analysis Project**

Overview

This project processes server log files to extract valuable insights such as the number of requests per IP address, the most accessed endpoints, and suspicious activity detection. The project also saves the results in a structured format for further analysis or reporting.

Features
Requests Per IP Address
Identifies the total number of requests made by each IP address and displays them in descending order of request count.

Most Accessed Endpoints
Analyzes the log file to find the most frequently accessed endpoints (e.g., URLs).

Suspicious Activity Detection
Flags IP addresses that exceed a specified threshold of failed login attempts (e.g., HTTP 401 status or specific error messages like "Invalid credentials").

Most Common Timestamp for Suspicious IPs
Extracts timestamps for flagged suspicious IPs and identifies the most common timestamp for each.

Export Results
Saves the analysis to a CSV file with structured sections:

Requests per IP
Most accessed endpoints
Suspicious activity data


**Code Details**

The script includes the following major components:

Counting Requests per IP Address:

Extracts IP addresses from each log entry and counts their occurrences.
Results are displayed in descending order.
Identifying Most Frequently Accessed Endpoint:

Parses the request section of each log entry to determine the endpoint.
Counts the frequency of each endpoint.
Detecting Suspicious Activities:

Tracks failed login attempts (status code 401) and flags IPs exceeding the threshold.
Monitors total requests per IP and flags high-volume requests.
Tracks unusually accessed endpoints.
Saving Results to CSV:

Organizes the data into structured sections for easy review and archival.

**How It Works**

Log File Reading
The script reads log entries from a log file (e.g., sample.log).

Data Extraction

Extracts IP addresses, request details, timestamps, and error messages.
Counts occurrences and detects anomalies.
Analysis

Finds top IPs based on request count.
Identifies the most accessed endpoints.
Flags suspicious IPs and extracts their timestamps.
Output

Displays results in a formatted terminal output.
Exports findings to log_analysis.csv.


**Key Learning Points**

File Handling 
string manipulation
Dictionaries
Sorting Strings
Thresholds
CSV Writing
Error Handling

