"""Calculate the day of the week for any given date."""

import sys
from datetime import datetime


def main():
    """Main function"""
    try:
        date = datetime.strptime(sys.argv[1], "%m-%d-%Y")
    except (IndexError, ValueError):
        print('You should enter a date in the "MM-DD-YYYY" format.')
        return
    print(f"The day of the week for {sys.argv[1]} is {date.strftime('%A')}.")


if __name__ == "__main__":
    main()
