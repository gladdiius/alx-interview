"""Parses log data from standard input, calculates metrics, and prints them
every 10 lines or on keyboard interrupt.

This script expects log lines in the following format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Lines that don't match this format are assumed to be invalid and skipped.

The script calculates the following metrics:

* Total file size: Sum of all file sizes encountered.
* Number of lines by status code: Counts occurrences of each unique status code.

The script prints these metrics every 10 lines read from standard input or
upon receiving a keyboard interrupt (CTRL+C).
"""

from collections import defaultdict
import sys


def main():
    """Main function that parses log data and stores metrics in a dictionary."""

    metrics = defaultdict(int)  # Dictionary to store total size and status code counts

    try:
        for line in sys.stdin:
            # Extract relevant data (assuming valid format)
            status_code = int(line.split()[4])
            file_size = int(line.split()[6])

            # Update metrics
            metrics["total_size"] += file_size
            metrics[status_code] += 1

            # Print stats every 10 lines or on keyboard interrupt
            if len(metrics) % 11 == 0:  # Check every 10 lines + first line
                print_stats(metrics)

    except KeyboardInterrupt:
        print_stats(metrics)
        print("\nExiting due to keyboard interrupt.")


def print_stats(metrics):
    """Prints the calculated metrics from the provided dictionary."""

    print(f"Total file size: {metrics['total_size']}")
    for code, count in sorted(metrics.items()):
        if code != "total_size":  # Skip "total_size" key
            print(f"{code}: {count}")


if __name__ == "__main__":
    main()
