#!/usr/bin/python3
"""updated"""
import sys


def print_statistics(total_size, status_counts):
    """
    Print statistics based on accumulated data.

    Args:
        total_size (int): Total accumulated file size.
        status_counts (dict): Dictionary mapping status codes to their counts.
    """
    print(f"File size: {total_size}")
    sorted_status_codes = sorted(status_counts.keys())
    for code in sorted_status_codes:
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def main():
    """
    Main function to read stdin, compute metrics, and print statistics.
    """
    total_size = 0
    status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            line = line.strip()
            parts = line.split()
            if len(parts) != 7:
                continue

            status_code = int(parts[-2])
            file_size = int(parts[-1])

            if status_code in status_counts:
                status_counts[status_code] += 1
            total_size += file_size

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
                total_size = 0
                status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    except KeyboardInterrupt:
        # If interrupted, print current statistics before exiting
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
