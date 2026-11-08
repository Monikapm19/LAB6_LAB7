import math
import re


def parse_setpoint(text):
    try:
        if not isinstance(text, str):
            return None

        text = text.strip()

        if len(text) < 2:
            return None

        unit = text[-1].upper()

        if unit not in ('C', 'F'):
            return None

        value = float(text[:-1])

        if not math.isfinite(value):
            return None

        if unit == 'F':
            value = (value - 32) * 5 / 9

        return round(value, 1)

    except (ValueError, TypeError, OverflowError):
        return None


def average_temperature(readings_csv):
    try:
        if not isinstance(readings_csv, str):
            return None

        readings = readings_csv.split(',')

        if not readings or any(not r.strip() for r in readings):
            return None

        values = [float(r.strip()) for r in readings]

        if not all(math.isfinite(v) for v in values):
            return None

        return sum(values) / len(values)

    except (ValueError, TypeError, OverflowError):
        return None


def schedule_slot(time_text):
    try:
        if not isinstance(time_text, str):
            return None

        time_text = time_text.strip()

        match = re.fullmatch(r'([0-9]{2}):([0-9]{2})', time_text)

        if not match:
            return None

        hour = int(match.group(1))
        minute = int(match.group(2))

        if hour > 23 or minute > 59:
            return None

        if hour < 6:
            return 'night ' + match.group(2)

        return 'day ' + str(minute)

    except (ValueError, TypeError, OverflowError):
        return None


def main():
    print("==== Running parse_setpoint ====")
    user_input = input("Enter a setpoint (e.g. 21.5C or 70F): ")
    result = parse_setpoint(user_input)
    print("Setpoint in Celsius:", result)

    print("\n==== Running average_temperature ====")
    user_input = input("Enter sensor readings as CSV (e.g. 20.5,21,22.5): ")
    result = average_temperature(user_input)
    print("Average Temperature:", result)

    print("\n==== Running schedule_slot ====")
    user_input = input("Enter a time as HH:MM (e.g. 07:30): ")
    result = schedule_slot(user_input)
    print("Schedule Slot:", result)


if __name__ == "__main__":
    main()