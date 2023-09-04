# Time-Calculator
TimeCalculator is a Python script that calculates the new time when a duration is added to a given starting time. It's a versatile tool that can handle both time additions and subtractions. This script is particularly useful when you need to determine the time after a specific duration, considering AM/PM and even days.
How it Works:

The add_time function takes three inputs:

- start: The starting time in the format "hh:mm AM/PM."
- duration: The duration to add or subtract in the format "hh:mm."
- day (optional): The starting day of the week (case insensitive).

Key Features:

- Handles both AM and PM time formats.
- Adjusts days if the duration extends beyond 24 hours.
- Supports specifying the starting day of the week for advanced time calculations.
