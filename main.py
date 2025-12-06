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

def to_year_month_day(date_str):
    for format in formats:
        try:
            dt = datetime.strptime(date_str, format)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            pass
    raise ValueError("Unknown date format: " + date_str)

while True:
    input_date = str(input("Enter Date to format: "))
    formatted_date = to_year_month_day(input_date)
    print(f"Formatted Date: {formatted_date}")
    pyperclip.copy(formatted_date)
    print("Text copied to clipboard.\nPress enter to start over, and format another date.")
    input()