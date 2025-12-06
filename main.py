import pyperclip
from datetime import datetime

formats = [
    "%B %d, %Y",   # November 1, 2013
    "%b %d, %Y",   # Nov 1, 2013
    "%b %d %Y",    # Nov 1 2013
    "%B %d %Y",    # November 1 2013
    "%m/%d/%Y",    # 11/01/2013
    "%m-%d-%Y",    # 11-01-2013
    "%Y-%m-%d",    # 2013-11-01
]

def to_year_month_day(date_str: str):
    # Check if the date is fully numeric (slashes or dashes)
    if all(ch.isdigit() or ch in "/-" for ch in date_str):
        separator = "/" if "/" in date_str else "-"
        parts = date_str.split(separator)

        # Must be exactly three parts
        if len(parts) == 3:
            a, b, c = parts
            if a.isdigit() and b.isdigit():
                a, b = int(a), int(b)

                # If ambiguous: both <= 12
                if 1 <= a <= 12 and 1 <= b <= 12:
                    print(f"\nAmbiguous date detected: {date_str}")
                    print("Both month and day are 12 or below.")
                    print("Which format is correct?")
                    print("1. MM/DD/YYYY")
                    print("2. DD/MM/YYYY")
                    
                    choice = input("Enter 1 or 2: ").strip()

                    if choice == "1":
                        dt = datetime.strptime(date_str, f"%m{separator}%d{separator}%Y")
                        return dt.strftime("%Y-%m-%d")
                    elif choice == "2":
                        dt = datetime.strptime(date_str, f"%d{separator}%m{separator}%Y")
                        return dt.strftime("%Y-%m-%d")
                    else:
                        raise ValueError("Invalid choice for ambiguous date.")

    # Try normal formats
    for format in formats:
        try:
            dt = datetime.strptime(date_str, format)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            pass

    raise ValueError("Unknown date format: " + date_str)


while True:
    input_date = input("Enter Date to format: ")
    formatted_date = to_year_month_day(input_date)
    print(f"Formatted Date: {formatted_date}")
    pyperclip.copy(formatted_date)
    print("Text copied to clipboard.\nPress enter to start over, and format another date.")
    input()