import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match the 12-hour time format
    pattern = r'^(\d{1,2}):(\d{2}) (AM|PM) to (\d{1,2}):(\d{2}) (AM|PM)$'
    match = re.match(pattern, s)

    if match:
        # Extracting hour, minute, and period (AM/PM) for start time
        start_hour = int(match.group(1))
        start_minute = int(match.group(2))
        start_period = match.group(3)

        # Extracting hour, minute, and period (AM/PM) for end time
        end_hour = int(match.group(4))
        end_minute = int(match.group(5))
        end_period = match.group(6)

        # Adjusting hours based on AM/PM
        if start_period == 'PM' and start_hour != 12:
            start_hour += 12
        if end_period == 'PM' and end_hour != 12:
            end_hour += 12

        # Validating the time range
        if start_hour > 23 or start_minute > 59 or end_hour > 23 or end_minute > 59:
            raise ValueError("Invalid time")

        # Formatting the time in 24-hour format
        start_time = f"{start_hour:02d}:{start_minute:02d}"
        end_time = f"{end_hour:02d}:{end_minute:02d}"

        return f"{start_time} to {end_time}"
    else:
        raise ValueError("Invalid time format")

if __name__ == "__main__":
    main()
