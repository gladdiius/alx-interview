#!/usr/bin/python3
import sys
from collections import defaultdict

# Initialize variables
total_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        # Check if line matches the expected format
        if len(parts) == 7 and parts[3].isdigit() and parts[-1].isdigit():
            status_code = int(parts[5])
            file_size = int(parts[6])

            # Update total file size
            total_size += file_size

            # Update status code counts
            status_code_counts[status_code] += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_code_counts.keys()):
                    if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                        print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        if code in [200, 301, 400, 401, 403, 404, 405, 500]:
            print(f"{code}: {status_code_counts[code]}")
